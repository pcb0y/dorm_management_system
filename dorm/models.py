from django.db import models

# Create your models here.
# 设置水费单价
default_water_price = 4.81
# 设置电费单价
default_electricity_price = 1.2


class BuildName(models.Model):
    """楼名"""
    build_name = models.CharField(max_length=30, null=True, verbose_name="楼名")

    def __str__(self):
        return self.build_name

    class Mate:
        verbose_name = "楼名"
        verbose_name_plural = verbose_name


class Floor(models.Model):
    floor_name = models.CharField(max_length=10, null=True, verbose_name="楼层")

    def __str__(self):
        return self.floor_name

    class Mate:
        verbose_name = "楼层"
        verbose_name_plural = verbose_name


class RoomCategory(models.Model):
    """房屋类别"""
    Room_Category_name = models.CharField(max_length=20, null=True, verbose_name="房屋类别")

    def __str__(self):
        return self.Room_Category_name

    class Meta:
        verbose_name = "房屋类别表"
        verbose_name_plural = verbose_name


class DeviceList(models.Model):
    """
    设备清单表
    """
    # 设备名称
    device_name = models.CharField(max_length=20, null=True, verbose_name="设备名称")
    # 设备价格
    device_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="设备价格")

    def __str__(self):
        return self.device_name

    class Meta:
        verbose_name = "设备清单表"
        verbose_name_plural = verbose_name


class Rent(models.Model):
    """
        租金分类表
    """
    # 租金单价
    rent_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="租金单价")

    def __str__(self):
        return str(self.rent_price)

    class Meta:
        verbose_name = "租金分类表"
        verbose_name_plural = verbose_name


class User(models.Model):
    """
        用户表
    """
    # 用户名
    user_name = models.CharField(max_length=20, verbose_name="用户名")
    # 密码
    password = models.CharField(max_length=100, verbose_name="密码")
    # 权限
    power = models.SmallIntegerField(verbose_name="权限", null=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


class RoomType(models.Model):
    """
        房屋类型表
    """
    # 房屋类型名称
    type_name = models.CharField(max_length=20, verbose_name="房屋类型")

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "房屋类型表"
        verbose_name_plural = verbose_name


class Room(models.Model):
    """
        房屋信息表
    """
    # 楼名
    build_name = models.ForeignKey(to=BuildName, null=True, on_delete=models.SET_NULL, verbose_name="楼名")
    # 楼层
    floor = models.ForeignKey(to=Floor, null=True, on_delete=models.SET_NULL, verbose_name="楼层")

    # 房间号
    room_number = models.CharField(max_length=10, verbose_name="房间号")
    # 入住人数
    number_of_people = models.SmallIntegerField(verbose_name="入住人数")
    # 配标人数
    standard_number_of_people = models.SmallIntegerField(verbose_name="配标人数")
    # 空床数
    empty_bed_number = models.SmallIntegerField(verbose_name="空床数")

    # 关联房类型表
    room_type = models.ForeignKey(to=RoomType, null=True, on_delete=models.SET_NULL, verbose_name="房屋类型")
    # 关联设备清单
    device_list = models.ForeignKey(to=DeviceList, null=True, on_delete=models.SET_NULL, verbose_name="设备清单")
    # 关联房屋类别清单
    room_category = models.ForeignKey(to=RoomCategory, null=True, on_delete=models.SET_NULL, verbose_name="房屋类别",
                                      )
    WaterElectricity_Balance = models.DecimalField(default=0, max_digits=20, decimal_places=2, verbose_name="水电费余额", null=True)
    # 是否启用
    is_used = models.BooleanField(default=True, verbose_name="是否启用")

    def __str__(self):
        return self.room_number

    class Meta:
        verbose_name = "房屋信息表"
        verbose_name_plural = verbose_name


class Department(models.Model):
    """
    部门信息表
    """
    # 部门名称
    department_name = models.CharField(max_length=20, verbose_name="部门名称")

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name = "部门信息表"
        verbose_name_plural = verbose_name


class BedNumber(models.Model):
    """床号"""
    bed_name = models.CharField(max_length=10, verbose_name="床号")

    def __str__(self):
        return self.bed_name

    class Meta:
        verbose_name = "床号表"
        verbose_name_plural = verbose_name


class People(models.Model):
    """
        人员信息表
    """
    # 姓名
    name = models.CharField(max_length=10, verbose_name="姓名")
    # 性别
    sex_choices = ((1, "男"), (0, "女"))
    sex = models.SmallIntegerField(choices=sex_choices, verbose_name="性别")
    # 手机
    phone = models.CharField(max_length=11, verbose_name="手机")
    # 关联部门表
    department = models.ForeignKey(to=Department, null=True, on_delete=models.SET_NULL, verbose_name="关联部门表")
    # 身份证号
    people_number = models.CharField(max_length=18, verbose_name="身份证号")
    # 关联床号
    bed_number = models.ForeignKey(to=BedNumber, null=True, on_delete=models.SET_NULL, verbose_name="床号")
    # 入住时间
    check_in_time = models.DateField(verbose_name="入住时间")
    # 结算时间
    Settlement_time = models.DateField(default=None, null=True, blank=True, verbose_name="结算时间")
    # 合同到期时间
    check_out_time = models.DateField(verbose_name="合同到期日期", null=True, blank=True)
    # 关联用户表
    user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL, verbose_name="录入人")
    # 押金
    deposit = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="押金")
    # 关联租金单价表
    rent_price = models.ForeignKey(to=Rent, null=True, on_delete=models.CASCADE, verbose_name="租金单价")
    balance = models.DecimalField(default=None, max_digits=20, decimal_places=2, verbose_name="余额", null=True)
    # 备注
    remark = models.CharField(max_length=11, null=True, blank=True, verbose_name="备注")
    # 关联房屋
    room = models.ForeignKey(to=Room,  null=True, on_delete=models.SET_NULL, related_name="people",
                             verbose_name="房间号")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "人员信息表"
        verbose_name_plural = verbose_name


class WaterElectricity(models.Model):
    """
      水电费明细表
    """
    # 关联房间
    room = models.ForeignKey(to=Room, null=True, on_delete=models.SET_NULL, verbose_name="房间编码")
    # 月数
    mouth = models.CharField(max_length=6, verbose_name="年月数")
    # 水费表码起
    start_water_code = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="水费表码起")
    # 水费表码止
    end_water_code = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="水费表码止")
    # 水表合计
    water_sum = models.DecimalField(max_digits=20, decimal_places=1, verbose_name="水表数")
    # 水费单价
    water_price = models.DecimalField(max_digits=20, decimal_places=2, default=default_water_price, verbose_name="水费单价")
    # 水费金额
    water_amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="水费金额")

    # 水费抄表时间
    water_time = models.DateTimeField(auto_now_add=True, verbose_name="水费抄表时间")

    # 电表表码起
    start_electricity_code = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="电表表码起")
    # 电表表码止
    end_electricity_code = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="电表表码止")
    # 电表合计
    electricity_sum = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="电表数")
    # 电费单价
    electricity_price = models.DecimalField(max_digits=20, decimal_places=2, default=default_electricity_price,
                                            verbose_name="电费单价")
    # 电费金额
    electricity_amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="电费金额")

    # 电费抄表时间
    electricity_time = models.DateTimeField(auto_now_add=True, verbose_name="电费抄表时间")
    # 应付总金额
    sum_amount = models.DecimalField(default=0, max_digits=20, decimal_places=2, verbose_name="应付总金额")
    # 扣款金额
    deduction_amount = models.DecimalField(default=None, max_digits=20, decimal_places=2, verbose_name="扣款金额")

    # 扣款时间
    deduction_time = models.DateTimeField(auto_now_add=True, verbose_name="扣款时间")
    # 修改时间
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    electricity_payment_user = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL, verbose_name="扣费人")
    # electricity_create_user = models.ForeignKey(to=User, default=1, on_delete=models.CASCADE, verbose_name="创建人")
    status = (
        (1, "已缴费"),
        (0, "未缴费")
    )
    payment_status = models.SmallIntegerField(default=0, choices=status, verbose_name="交费状态")
    # 扣款原因
    deduction_reason = models.CharField(default=None, max_length=30, null=True, blank=True, verbose_name="扣款原因")
    remark = models.CharField(default=None, max_length=100, null=True, blank=True, verbose_name="备注")

    def __str__(self):
        return str(self.sum_amount)

    class Meta:
        verbose_name = "水电费明细表"
        verbose_name_plural = verbose_name


class RentDetails(models.Model):
    """
        租金明细表
    """
    # 关联员工信息表people
    people = models.ForeignKey(to=People, null=True,  on_delete=models.CASCADE, verbose_name="姓名")

    year_month = models.CharField(max_length=100, null=True, blank=True, verbose_name="年月数")
    # 应缴金额
    payable_amount = models.DecimalField(default=0, max_digits=20, decimal_places=2, verbose_name="应缴金额")

    # 扣款金额
    deduction_amount = models.DecimalField(default=0, max_digits=20, decimal_places=2, verbose_name="扣款金额")

    # 扣款时间
    deduction_time = models.DateTimeField(auto_now_add=True, verbose_name="扣款时间")
    # 修改时间
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    payment_user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="payment_user", verbose_name="扣费人")
    create_user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="创建人")
    status = (
        (1, "已缴费"),
        (0, "未缴费")
    )
    payment_status = models.SmallIntegerField(default=0, choices=status, verbose_name="交费状态")
    # 扣款原因
    deduction_reason = models.CharField(default=None, max_length=30, null=True, blank=True, verbose_name="扣款原因")
    # 备注
    remark = models.CharField(default=None, max_length=100, null=True, blank=True, verbose_name="备注")

    def __str__(self):
        return self.balance

    class Meta:
        verbose_name = "租金明细表"
        verbose_name_plural = verbose_name


class RepairReport(models.Model):
    """
    维修明细表
    """
    # 关联报修人表
    people = models.ForeignKey(to=People, on_delete=models.CASCADE, verbose_name="报修人")
    # 关联房屋表
    room = models.ForeignKey(to=Room,  on_delete=models.CASCADE, verbose_name="房间号")
    # 报修日期
    repair_time = models.DateTimeField(verbose_name="报修日期")
    # 关联报修设备表
    repair_device = models.ForeignKey(to=DeviceList,   on_delete=models.CASCADE, verbose_name="维修设备")
    # 故障说明
    fault_description = models.CharField(max_length=50, null=True, verbose_name="故障说明")
    # 是否保质期内
    is_quality_guarantee_period = models.BooleanField(null=True, verbose_name="是否保质期内")
    # 维修费用
    repair_cost = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name="维修费用")
    # 是否自费
    is_self_cost = models.BooleanField(null=True, verbose_name="是否自费")
    # 维修人
    repair_people = models.CharField(max_length=10, null=True, blank=True, verbose_name="维修人")
    # 是否修好
    is_repaired = models.BooleanField(default=False, verbose_name="是否修好")
    # 修复日期
    repair_date = models.DateField(null=True, blank=True, verbose_name='修复日期')
    # 备注
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name="备注")

    def __str__(self):
        return self.is_repaired

    class Meta:
        verbose_name = "维修明细表"
        verbose_name_plural = verbose_name


class DeviceDetail(models.Model):
    """设备详情表"""

    room = models.ForeignKey(to=Room, on_delete=models.CASCADE, verbose_name="房间号")
    device_name = models.ForeignKey(to=DeviceList, on_delete=models.SET_NULL, null=True, verbose_name="设备名称")
    device_number = models.IntegerField(default=1, verbose_name="设备数量")
    remark = models.CharField(max_length=50, null=True, blank=True, verbose_name="备注")

    def __str__(self):
        return self.device_name

    class Meta:
        verbose_name = "设备详情表"
        verbose_name_plural = verbose_name


class Payment(models.Model):
    """付款记录表"""

    people = models.ForeignKey(to=People, on_delete=models.CASCADE, verbose_name="付款人")
    # 实缴金额
    actual_amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="实缴金额")

    # 缴费时间
    payment_time = models.DateTimeField(auto_now_add=True, verbose_name="缴费时间")
    # 修改时间
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    create_user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="创建人")
    # 备注
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name="备注")

    def __str__(self):
        return str(self.actual_amount)

    class Meta:
        verbose_name = "付款记录表"
        verbose_name_plural = verbose_name


class PaymentWaterElectricity(models.Model):
    """付款水电费记录表"""

    room_number = models.ForeignKey(to=Room, on_delete=models.CASCADE, verbose_name="房间号")
    # 实缴金额
    actual_amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="实缴金额")

    # 缴费时间
    payment_time = models.DateTimeField(auto_now_add=True, verbose_name="缴费时间")
    # 修改时间
    modified_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    create_user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="创建人")
    # 备注
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name="备注")

    def __str__(self):
        return str(self.actual_amount)

    class Meta:
        verbose_name = "付款水电费记录表"
        verbose_name_plural = verbose_name






