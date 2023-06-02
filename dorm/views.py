from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from dorm.Serializer import *
from dorm import models
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
# class PeoplesView(ModelViewSet):
#     queryset = models.People.objects.all()
#     serializer_class = PeoplesSerializers
