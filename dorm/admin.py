from django.contrib import admin
from django.contrib import admin
from .models import *

admin.site.register(RoomCategory)
admin.site.register(DeviceList)
admin.site.register(User)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Department)
admin.site.register(BedNumber)
admin.site.register(People)
admin.site.register(WaterElectricity)
admin.site.register(Rent)
admin.site.register(RentDetails)
admin.site.register(RepairReport)
admin.site.register(DeviceDetail)
admin.site.register(Payment)


admin.site.site_header = '慕宸宿舍管理系统'
admin.site.site_title = '慕宸宿舍管理系统'
admin.site.index_title = '后台管理'
