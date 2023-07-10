from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from dorm.Serializer import *
from dorm import models
from datetime import date
from dateutil.relativedelta import relativedelta
import calendar
from decimal import Decimal
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from django.db.models import Count, Sum, Max, Min, Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
import jwt
from jwt import exceptions
import datetime
import uuid
from django.conf import settings
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
import datetime
from .jwt_create_token import create_token
from .jwt_authenticate import JWTQueryParamsAuthentication
from rest_framework.pagination import PageNumberPagination
import pandas as pd
from rest_framework import generics
# Create your views here.


# 定义分页类
class MyPageNumberPagination(PageNumberPagination):
    # 分页数量
    page_size = 20


class LoginView(APIView):
    """用户登录"""
    authentication_classes = []  # 取消全局认证

    def post(self, request, *args, **kwargs):
        user = request.data.get('username')
        pwd = request.data.get('password')
        user_obj = User.objects.filter(user_name=user).first()
        # print(user_obj)
        if not user_obj:
            return Response({'code': 401, 'error': '用户名或密码错误'})

        payload = {
            'user_id': user_obj.pk,  # 自定义用户ID
            'username': user_obj.user_name,  # 自定义用户名
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=1),  # 设置超时时间，1min
        }
        jwt_token = create_token(payload=payload)
        return Response({'code': 200, 'token': jwt_token})

# {"username":"admin","password":"admin123"}


class IndexView(APIView):
    """"局部认证"""
    authentication_classes = [JWTQueryParamsAuthentication, ]

    @staticmethod
    def get(self,request,*args,**kwargs):
        return Response("可以了")


class TokenView(APIView):
    authentication_classes = []  # 取消全局认证

    def post(self,request,*args,**kwargs):
        """用户登陆"""
        # print(request.data)
        user = request.data.get("username")
        # print(user)
        # 用户输入的密码
        input_pwd = request.data.get("password")

        # 加密过存到数据库的密码
        hashed_password = User.objects.filter(user_name=user).values("password")[0]["password"]
        # 匹配密码

        password_matched = check_password(input_pwd, hashed_password)
        # print("密码匹配",password_matched,type(input_pwd),hashed_password)
        if not password_matched:
            return Response({"code": 401, "error": "用户名或密码错误"})
        salt = settings.SECRET_KEY
        # 构造Header，默认如下
        headers = {
            'typ': 'jwt',
            'alg': 'HS256'
        }
        # 构造Payload
        payload = {

            "username": user,  # 自定义用户名
            "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=60*24)
        }

        jwt_token = jwt.encode(headers=headers, payload=payload, key=salt, algorithm="HS256")
        return Response({'code': 200, 'token': jwt_token, 'username': user})


class LoginView(APIView):

    def get(self, request, *args, **kwargs):
        token = request.query_params.get("token")
        salt = settings.SECRET_KEY
        print(token, salt)
        payload=None
        error = ""
        try:
            # 从token中获取payload【不校验合法性】
            # unverified_payload = jwt.decode(token, None, False)
            # print(unverified_payload)
            # 从token中获取payload【校验合法性】
            payload = jwt.decode(token, salt, verify=True, algorithms="HS256")
            print(payload)
            return Response(f"已登录成功，欢迎！")
        except exceptions.ExpiredSignatureError:
            error = "token已失效"
            return Response({"code": 401, "error": error})
        except jwt.DecodeError:
            error = "token认证失败"
            print(payload)
            return Response({"code": 401, "error": error})
        except jwt.InvalidTokenError:
            error = "非法token"
            return Response({"code": 401, "error": error})
        if not payload:
            return Response({"code": 1003})


class RoomView(ModelViewSet):

    """ 房屋管理视图"""
    queryset = models.Room.objects.all()
    # serializer_class = RoomSerializers
    pagination_class = MyPageNumberPagination
    ordering = ['-id']

    # 进行条件查询
    def get_queryset(self):
        queryset = super().get_queryset()
        room_number = self.request.query_params.get('room_number')
        if room_number:
            queryset = queryset.filter(room_number=room_number)
        return queryset.order_by('-id')
    # 根据不同的请求走不同的序列化器

    def get_serializer_class(self):
        if self.action == "list":
            return RoomSerializers
        else:
            return RoomsSerializers


class PeopleView(ModelViewSet):
    """人员管理视图"""
    queryset = models.People.objects.all()
    serializer_class = PeopleSerializers
    pagination_class = MyPageNumberPagination
    ordering = ['-id']

    # 进行条件查询
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset.order_by('-id')

    # 重写perform_create方法更新房间信息入住人数字段
    def perform_create(self, serializer):
        instance = serializer.save()
        # 获取房间的实例
        related_instance = instance.room
        # related_instance.number_of_people = related_instance.standard_number_of_people-1
        # 获取房间的ID
        room_id = related_instance.id
        # 查找房间住的人数
        room_in_people = models.People.objects.filter(room_id=room_id).count()
        # print(room_in_people)
        # 更新房间表人数
        related_instance.number_of_people = room_in_people
        related_instance.empty_bed_number = related_instance.standard_number_of_people-room_in_people
        related_instance.save()


class WaterElectricityView(ModelViewSet):
    """水电管理视图"""
    queryset = models.WaterElectricity.objects.all()
    serializer_class = WaterElectricitySerializers
    pagination_class = MyPageNumberPagination

    # 进行条件查询
    def get_queryset(self):
        queryset = super().get_queryset()
        room_number = self.request.query_params.get('room_number')
        if room_number:
            queryset = queryset.filter(room__room_number=room_number)
        return queryset.order_by("-id")


class RentDetailsView(ModelViewSet):
    """租金管理视图"""

    queryset = models.RentDetails.objects.all()
    serializer_class = RentDetailsSerializers
    pagination_class = MyPageNumberPagination
    # sql = queryset.query.__str__()
    # print(sql)


class RepairReportView(ModelViewSet):
    """维修管理视图"""
    queryset = models.RepairReport.objects.all()
    serializer_class = RepairReportSerializers
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        """倒序排列"""
        queryset = super().get_queryset()

        return queryset.order_by('-id')


class DeviceDetailView(ModelViewSet):
    """设备管理视图"""
    queryset = models.DeviceDetail.objects.all()
    serializer_class = DeviceDetailSerializers
    pagination_class = MyPageNumberPagination


class BuildNameView(ModelViewSet):
    """楼名视图"""
    queryset = models.BuildName.objects.all()
    serializer_class = BuildNameSerializers


class FloorView(ModelViewSet):
    """楼层视图"""
    queryset = models.Floor.objects.all()
    serializer_class = FloorSerializers


class RoomTypeView(ModelViewSet):
    """房屋类型视图"""
    queryset = models.RoomType.objects.all()
    serializer_class = RoomTypeSerializers


class RoomCategoryView(ModelViewSet):
    """房屋类别视图"""
    queryset = models.RoomCategory.objects.all()
    serializer_class = RoomCategorySerializers


class DepartmentView(ModelViewSet):
    """部门视图"""
    queryset = models.Department.objects.all()
    serializer_class = DepartmentSerializers


class BedNumberView(ModelViewSet):
    """床号视图"""
    queryset = models.BedNumber.objects.all()
    serializer_class = BedNumberSerializers


class RoomNumberView(ModelViewSet):
    """房间号视图"""
    queryset = models.Room.objects.all()
    serializer_class = RoomNumberSerializers


class PeopleNameView(ModelViewSet):
    """人员姓名视图"""
    queryset = models.People.objects.all()
    serializer_class = PeopleNameSerializers


class UserView(ModelViewSet):
    """用户视图"""
    queryset = models.User.objects.all()
    serializer_class = UserSerializers

    # 创建用户加密
    def create(self, request, *args, **kwargs):
        user = request.data.get("user_name")
        user_obj = User.objects.filter(user_name=user).first()
        if user_obj:
            return Response({"code": 402, "error": "该用户已经注册,请更换帐号!"})
        password = request.data.get("password")

        hashed_password = make_password(password)
        request.data['password'] = hashed_password
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeviceListView(ModelViewSet):
    """设备清单视图"""
    queryset = models.DeviceList.objects.all()
    serializer_class = DeviceListSerializers


class AddRentDetailsView(APIView):
    @staticmethod
    def get(self):
        peoples = models.People.objects.all().values("id", "rent_price__rent_price", "check_in_time")
        user = models.User.objects.filter(pk=5).first()

        device_obj_list = []
        for people in peoples:
            # 获取当前日期
            current_date = datetime.date.today()

            # 获取上个月的年份和月份
            previous_month = current_date.month - 1
            previous_year = current_date.year

            # 如果当前月份是 1 月，则上个月为去年的 12 月
            if previous_month == 0:
                previous_month = 12
                previous_year -= 1

            # 获取上个月的天数
            num_days = calendar.monthrange(previous_year, previous_month)[1]

            # 获取入住时间和当前时间的月份差
            months_diff = relativedelta(date.today(), people['check_in_time'])
            # print(months_diff.months)
            if months_diff.months == 0:

                # 按天算租金

                days_diff = date.today() - people['check_in_time']
                print(days_diff.days)
                payable_amount = days_diff.days*people["rent_price__rent_price"]/num_days

            else:
                # 按月算租金
                payable_amount = people["rent_price__rent_price"]
            if previous_month < 10:
                previous_month = "0" + str(previous_month)
            year_month = str(previous_year)+previous_month
            print(year_month)
            # print(months_diff.months)
            device_obj_list.append(
                RentDetails(
                    year_month=year_month, people_id=people["id"], payable_amount=payable_amount, create_user=user
                )
            )
        models.RentDetails.objects.bulk_create(device_obj_list)
        return HttpResponse("生成租金帐单明细成功")


class PaymentView(ModelViewSet):
    """付款视图"""

    queryset = models.Payment.objects.all()
    serializer_class = PaymentSerializers
    pagination_class = MyPageNumberPagination

    # 进行条件查询
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(people__name=name)
        queryset = queryset.order_by("-id")
        return queryset

    def create(self, request):
        people = self.request.data.get("people")
        actual_amount = self.request.data.get("actual_amount")
        obj = models.People.objects.get(pk=people)

        obj.balance += Decimal(actual_amount)
        obj.save()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeductionView(ModelViewSet):
    """扣租金视图"""
    queryset = models.RentDetails.objects.all()
    serializer_class = DeductionSerializers

    def update(self, request, pk):

        # print(pk)
        # 获取数据库中扣费的字段如果为空,就不扣费直接返回
        deduction_amount_db = models.RentDetails.objects.filter(pk=pk).values("deduction_amount")
        # print(deduction_amount_db)
        if deduction_amount_db[0].get("deduction_amount"):
            return_data = {"message": "已经交过费了不允许重复扣费"}
            return Response(return_data)
        instance = self.get_object()
        # print(request.data)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # 获取前端传递的参数
        deduction_amount = serializer.validated_data.get("deduction_amount")
        # print(deduction_amount)
        # 修改表中的数据
        instance.deduction_amount = deduction_amount
        instance.payment_status = 1
        instance.save()
        # 更新人员表的余额
        instance.people.balance -= deduction_amount
        instance.people.save()
        return Response(serializer.data)


class PaymentWaterElectricityView(ModelViewSet):
    """充值水电费视图"""
    queryset = models.PaymentWaterElectricity.objects.all()
    serializer_class = PaymentWaterElectricitySerializers
    pagination_class = MyPageNumberPagination
    # 进行条件查询

    def get_queryset(self):
        queryset = super().get_queryset()
        room_number = self.request.query_params.get('room_number')
        # print(room_number)
        if room_number:
            queryset = queryset.filter(room_number__room_number=room_number)
        queryset = queryset.order_by("-id")
        return queryset

    def create(self, request):
        room_number = self.request.data.get("room_number")
        actual_amount = self.request.data.get("actual_amount")
        obj = models.Room.objects.get(pk=room_number)

        obj.WaterElectricity_Balance += Decimal(actual_amount)
        obj.save()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DeductionWaterElectricityView(ModelViewSet):
    """扣水电费视图"""
    queryset = models.WaterElectricity.objects.all()
    serializer_class = DeductionWaterElectricitySerializers

    def update(self, request, pk):

        # print(pk)
        # 获取数据库中扣费的字段如果为空,就不扣费直接返回
        deduction_amount_db = models.WaterElectricity.objects.filter(pk=pk).values("deduction_amount")
        # print(deduction_amount_db)
        if deduction_amount_db[0].get("deduction_amount"):
            return_data = {"message": "已经交过费了不允许重复扣费"}
            return Response(return_data)
        instance = self.get_object()
        # print(request.data)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # 获取前端传递的参数
        deduction_amount = serializer.validated_data.get("deduction_amount")
        # print(deduction_amount)
        # 修改表中的数据
        instance.deduction_amount = deduction_amount
        instance.payment_status = 1
        instance.save()
        # 更新人员表的余额
        instance.room.WaterElectricity_Balance -= deduction_amount
        instance.room.save()
        return Response(serializer.data)


class CountView(APIView):
    """统计视图"""
    def get(self,request):
        data = {}
        # 统计总房间数
        room_count = models.Room.objects.aggregate(room_count=Count('id'))
        # 统计已入住人数
        people_sum = models.People.objects.exclude(room=None).aggregate(people_sum=Count('id'))

        # 统计可住人数

        room_total_people = models.Room.objects.aggregate(room_total_people=Sum('standard_number_of_people'))

        # 统计空房间数
        empty_room = models.Room.objects.filter(people__room_id=None).count()

        # 统计空床数
        empty_bed_number = models.Room.objects.aggregate(empty_bed_number=Sum('empty_bed_number'))
        data.update(**room_count, **people_sum, **room_total_people, **empty_bed_number)
        data["empty_room"] = empty_room

        # print(data)
        return JsonResponse(data, safe=False)
        # return HttpResponse(data)


class UpdateRoomPeopleView(APIView):
    """更新房间表人数"""
    def get(self,request):
        room_id = models.Room.objects.all().values("id", "standard_number_of_people")
        # print(room_id.id)
        for i in room_id:
            # print(i["id"])
            room_in_people = models.People.objects.filter(room_id=i["id"]).count()
            models.Room.objects.filter(id=i["id"]).update(number_of_people=room_in_people,
                                                          empty_bed_number=i["standard_number_of_people"]-room_in_people)
            # print(room_in_people)
        return HttpResponse("ok")


class CheckInRecordView(ModelViewSet):
    """入住记录视图"""
    queryset = models.CheckInRecord.objects.all()
    serializer_class = CheckInRecordSerializers
    pagination_class = MyPageNumberPagination

    # 进行条件查询

    def get_queryset(self):
        queryset = super().get_queryset()
        room_number = self.request.query_params.get('room_number')
        name = self.request.query_params.get('name')
        # print(room_number)
        if room_number:
            queryset = queryset.filter(room__room_number=room_number)
        if name:
            queryset = queryset.filter(people__name=name)
        queryset = queryset.order_by("-id")

        return queryset


class CheckoutView(APIView):
    """退房视图"""

    def put(self, request,id):

        # 更新人员房间号字段为空,更新状态为退房状态
        res = models.People.objects.filter(id=id).update(room=None, check_in_stats=0 )


        return Response({"status": res})


class ImportWaterElectricityView(generics.CreateAPIView):
    """批量导入水电费视图"""
    serializer_class = WaterElectricitySerializers

    def create(self, request):

        file = request.FILES.get('file')

        df = pd.read_excel(file)

        serializer = self.get_serializer(data=df.to_dict(orient='records'), many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=201, headers=headers)
