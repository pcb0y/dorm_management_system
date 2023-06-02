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
        exclude = ["password", "power", "create_time"]


class RoomNumberSerializers(serializers.ModelSerializer):
    """房间号序列化器"""
    class Meta:
        model = Room
        fields = ["id", "room_number"]

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
    department_name = serializers.CharField(read_only=True, source="department.department_name")
    bed_number_name = serializers.CharField(read_only=True, source="bed_number.bed_name")
    user_name = serializers.CharField(read_only=True, source="user.user_name")
    room_name = serializers.CharField(read_only=True, source="room.room_number")
    remark = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = People
        fields = "__all__"
        # depth = 1


class RoomsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    """房屋管理序列化器"""
    # room_name = serializers.CharField(source="room.room_number")
    # room_name = PeopleSerializers(many=True, allow_null=True)
    # category_names = RoomCategorySerializers(many=True, read_only=True)
    # room_category_name = serializers.CharField(source="room_category.Room_Category_name")
    # room_type_name = serializers.CharField(source="room_type.type_name")

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1


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


class BuildNameSerializers(serializers.ModelSerializer):
    """楼名列化器"""

    class Meta:
        model = BuildName
        fields = "__all__"


class FloorSerializers(serializers.ModelSerializer):
    """楼层序列化器"""

    class Meta:
        model = Floor
        fields = "__all__"


class RoomTypeSerializers(serializers.ModelSerializer):
    """房屋类型序列化器"""

    class Meta:
        model = RoomType
        fields = "__all__"
# class BuildNameSerializers(serializers.ModelSerializer):
#     """楼名序列化器"""
#
#     class Meta:
#         model = BuildName
#         fields = "__all__"

