from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from dorm.Serializer import *
from dorm import models
from datetime import date
from dateutil.relativedelta import relativedelta
import calendar
from decimal import Decimal
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


class LoginView(APIView):
    """用户登录"""
    authentication_classes = []  # 取消全局认证

    def post(self, request, *args, **kwargs):
        user = request.data.get('username')
        pwd = request.data.get('password')
        user_obj = User.objects.filter(user_name=user, password=pwd).first()
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


# class TokenView(APIView):
#
#     def post(self,request,*args,**kwargs):
#         """用户登陆"""
#         user = request.data.get("username")
#         print(user)
#         pwd = request.data.get("password")
#         user_obj = User.objects.filter(user_name=user, password=pwd).first()
#         if not user_obj:
#             return Response({"code": 401, "error": "用户名或密码错误"})
#         salt = settings.SECRET_KEY
#         # 构造Header，默认如下
#         headers = {
#             'typ': 'jwt',
#             'alg': 'HS256'
#         }
#         # 构造Payload
#         payload = {
#             "user_id": user_obj.pk,  # 自定义用户ID
#             "username": user_obj.user_name,  # 自定义用户名
#             "exp": datetime.datetime.utcnow()+datetime.timedelta(minutes=5)
#         }
#         jwt_token = jwt.encode(headers=headers, payload=payload, key=salt, algorithm="HS256")
#         return Response({'code': 200, 'token': jwt_token})
#
#
# class LoginView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         token = request.query_params.get("token")
#         salt = settings.SECRET_KEY
#         print(token, salt)
#         payload=None
#         error = ""
#         try:
#             # 从token中获取payload【不校验合法性】
#             # unverified_payload = jwt.decode(token, None, False)
#             # print(unverified_payload)
#             # 从token中获取payload【校验合法性】
#             payload = jwt.decode(token, salt, verify=True, algorithms="HS256")
#             print(payload)
#             return Response(f"已登录成功，欢迎！")
#         except exceptions.ExpiredSignatureError:
#             error = "token已失效"
#             return Response({"code": 401, "error": error})
#         except jwt.DecodeError:
#             error = "token认证失败"
#             print(payload)
#             return Response({"code": 401, "error": error})
#         except jwt.InvalidTokenError:
#             error = "非法token"
#             return Response({"code": 401, "error": error})
#         if not payload:
#             return Response({"code": 1003})


class RoomView(ModelViewSet):

    """ 房屋管理视图"""
    queryset = models.Room.objects.all()
    # serializer_class = RoomSerializers
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


class WaterElectricityView(ModelViewSet):
    """水电管理视图"""
    queryset = models.WaterElectricity.objects.all()
    serializer_class = WaterElectricitySerializers


class RentDetailsView(ModelViewSet):
    """租金管理视图"""

    queryset = models.RentDetails.objects.all()
    serializer_class = RentDetailsSerializers
    # sql = queryset.query.__str__()
    # print(sql)


class RepairReportView(ModelViewSet):
    """维修管理视图"""
    queryset = models.RepairReport.objects.all()
    serializer_class = RepairReportSerializers


class DeviceDetailView(ModelViewSet):
    """设备管理视图"""
    queryset = models.DeviceDetail.objects.all()
    serializer_class = DeviceDetailSerializers


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


class UserView(ModelViewSet):
    """用户视图"""
    queryset = models.User.objects.all()
    serializer_class = UserSerializers


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
        return HttpResponse("kkk")


class PaymentView(ModelViewSet):
    """付款视图"""

    queryset = models.Payment.objects.all()
    serializer_class = PaymentSerializers

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
