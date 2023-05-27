from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from dorm.Serializer import *
from dorm import models
# Create your views here.


class RoomView(ModelViewSet):
    """ 房屋管理视图"""
    queryset = models.Room.objects.all()

    serializer_class = RoomSerializers


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
# class PeoplesView(ModelViewSet):
#     queryset = models.People.objects.all()
#     serializer_class = PeoplesSerializers
