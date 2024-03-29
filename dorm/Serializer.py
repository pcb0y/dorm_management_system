from rest_framework import serializers
from dorm.models import *

# 定义房屋类别序列化器


class RoomCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = "__all__"

# 定义用户表序列化器


class RentPriceSerializers(serializers.ModelSerializer):
    """租金单价序列化器"""
    class Meta:
        model = Rent
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = ["power", "create_time"]


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
    rent_price_name = serializers.CharField(read_only=True, source="rent_price.rent_price")
    remark = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = People
        fields = "__all__"
        # depth = 1


class PeopleNameSerializers(serializers.ModelSerializer):
    """人员姓名序列化器"""

    class Meta:
        model = People
        fields = ["id", "name"]
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
    people = PeopleSerializers(many=True)

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1


class RentDetailsSerializers(serializers.ModelSerializer):
    """租金管理序列化器"""
    create_user_name = serializers.CharField(read_only=True, source="create_user.user_name")
    payment_user_name = serializers.CharField(read_only=True, source="payment_user.user_name")
    name = serializers.CharField(read_only=True, source="people.name")
    room_number = serializers.CharField(read_only=True, source="people.room.room_number")
    rent_price = serializers.CharField(read_only=True, source="people.rent_price")
    balance = serializers.CharField(read_only=True, source="people.balance")

    class Meta:
        model = RentDetails
        fields = "__all__"
        # depth = 1


class RepairReportSerializers(serializers.ModelSerializer):
    """维修管理序列化器"""
    # room_people = serializers.CharField(source="people.name")
    # repair_device_name = serializers.CharField(source="repair_device.device_name")
    room_number = serializers.CharField(read_only=True, source="room.room_number")
    name = serializers.CharField(read_only=True, source="people.name")
    device_name = serializers.CharField(read_only=True, source="repair_device.device_name")

    class Meta:
        model = RepairReport
        fields = "__all__"
        # depth = 1


class WaterElectricitySerializers(serializers.ModelSerializer):
    """水电管理序列化器"""
    room = serializers.CharField(read_only=True)
    room_category = serializers.CharField(read_only=True, source="room.room_category")
    room_id = serializers.IntegerField(label="房间ID")
    WaterElectricity_Balance = serializers.CharField(read_only=True, source="room.WaterElectricity_Balance")
    electricity_payment_user = serializers.CharField(read_only=True)

    class Meta:
        model = WaterElectricity
        fields = "__all__"
        # depth = 1


class DeviceDetailSerializers(serializers.ModelSerializer):
    """设备详情序列化器"""
    room_id = serializers.IntegerField(label="房间号ID")
    device_name_id = serializers.IntegerField(label="设备ID")

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


class DeviceListSerializers(serializers.ModelSerializer):
    """设备清单序列化器"""
    value = serializers.IntegerField(read_only=True, source='id')
    text = serializers.CharField(read_only=True, source='device_name')

    class Meta:
        model = DeviceList
        fields = "__all__"


class PaymentSerializers(serializers.ModelSerializer):
    """付款序列化器"""

    class Meta:
        model = Payment
        fields = "__all__"
        depth = 1


class DeductionSerializers(serializers.ModelSerializer):
    """扣款序列化器"""

    class Meta:
        model = RentDetails
        fields = ["deduction_amount"]


class PaymentWaterElectricitySerializers(serializers.ModelSerializer):
    """水电费充值序列化器"""
    room_number = serializers.CharField(read_only=True, source="room_number.room_number")
    user_name = serializers.CharField(read_only=True, source="create_user.user_name")

    class Meta:
        model = PaymentWaterElectricity
        fields = "__all__"
        # depth = 1


class DeductionWaterElectricitySerializers(serializers.ModelSerializer):
    """扣款水电费序列化器"""

    class Meta:
        model = WaterElectricity
        fields = ["deduction_amount"]


class CheckInRecordSerializers(serializers.ModelSerializer):
    """入住记录序列化器"""

    room_number = serializers.CharField(read_only=True, source="room.room_number")
    people_name = serializers.CharField(read_only=True, source="people.name")
    user_name = serializers.CharField(read_only=True, source="create_user.user_name")

    class Meta:
        model = CheckInRecord
        fields = "__all__"


class CheckoutSerializers(serializers.ModelSerializer):
    """退房序列化器"""

    class Meta:
        model = People
        fields = ["id", "check_in_stats", "room"]


