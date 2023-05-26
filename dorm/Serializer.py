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


class RoomSerializers(serializers.ModelSerializer):
    """房屋管理序列化器"""
    class Meta:
        model = Room
        fields = "__all__"


class PeopleSerializers(serializers.ModelSerializer):
    """人员管理序列化器"""
    class Meta:
        model = People
        fields = "__all__"


class RentDetailsSerializers(serializers.ModelSerializer):
    """租金管理序列化器"""
    class Meta:
        model = RentDetails
        fields = "__all__"


class RepairReportSerializers(serializers.ModelSerializer):
    """维修管理序列化器"""
    class Meta:
        model = RepairReport
        fields = "__all__"
# class PeoplesSerializers(serializers.ModelSerializer):
#     room = RoomSerializers(many=True, read_only=True)
#     departments = DepartmentSerializers(many=True, read_only=True)
#     beds = BedNumberSerializers(many=True, read_only=True)
#     users = UserSerializers(many=True, read_only=True)
#
#     class Meta:
#         model = People
#         fields = ["id", "room", "departments", "beds", "users"]
