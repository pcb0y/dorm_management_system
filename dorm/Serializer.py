from rest_framework import serializers
from dorm.models import *

# 定义房屋类别序列化器


class RoomCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = "__all__"

# 定义用户表序列化器


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# 定义床号序列化器


class BedNumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = BedNumber
        fields = "__all__"

# 定义部门表序列化器


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

# 定义序列化器


class PeopleSerializers(serializers.ModelSerializer):
    """人员管理序列化器"""
    class Meta:
        model = People
        fields = "__all__"
        depth = 1


class RoomSerializers(serializers.ModelSerializer):
    """房屋管理序列化器"""
    room_name = PeopleSerializers(many=True)
    # category_names = RoomCategorySerializers(many=True, read_only=True)
    room_category_name = serializers.CharField(source="room_category.Room_Category_name")
    room_type_name = serializers.CharField(source="room_type.type_name")

    class Meta:
        model = Room
        fields = ["id", "build_name", "floor", "room_number", "number_of_people", "standard_number_of_people",
                  "empty_bed_number", "is_used", "room_type_name", "device_list",  "room_category_name", "room_name"]


class RentDetailsSerializers(serializers.ModelSerializer):
    """租金管理序列化器"""
    name = serializers.CharField(source="people.name")
    payee = serializers.CharField(source="payee.user_name")
    rent_price = serializers.DecimalField(max_digits=20, decimal_places=2, source="rent_price.rent_price")

    class Meta:
        model = RentDetails
        fields = "__all__"


class RepairReportSerializers(serializers.ModelSerializer):
    """维修管理序列化器"""
    # room_people = serializers.CharField(source="people.name")
    # repair_device_name = serializers.CharField(source="repair_device.device_name")
    # room_number = serializers.CharField(source="")
    class Meta:
        model = RepairReport
        fields = "__all__"
        depth = 1



class WaterElectricitySerializers(serializers.ModelSerializer):
    """水电管理序列化器"""

    class Meta:
        model = WaterElectricity
        fields = "__all__"
        depth = 1


class DeviceDetailSerializers(serializers.ModelSerializer):
    """设备详情序列化器"""

    class Meta:
        model = DeviceDetail
        fields = "__all__"
        depth = 1
