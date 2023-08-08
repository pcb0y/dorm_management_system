"""dorm_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from dorm import views
from rest_framework.routers import DefaultRouter  # 导入路由器定义的包


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', views.TokenView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('AddRentDetails/', views.AddRentDetailsView.as_view()),
    path('Count/', views.CountView.as_view()),
    path('updateRoomPeople/', views.UpdateRoomPeopleView.as_view()),
    path('Checkout/<int:id>/', views.CheckoutView.as_view()),  # 退房
    path('ImportWaterElectricity/', views.ImportWaterElectricityView.as_view()),  # 批量导入水电费
    path('ExportWaterElectricity/', views.ExportWaterElectricityView.as_view()),  # 导出水电费应付总金额
    path('ExportWaterElectricityAll/', views.ExportWaterElectricityAllView.as_view()),  # 导出水电费应付总金额
    path('ExportRoom/', views.ExportRoomView.as_view()),  # 导出房间人员
    path('EveryFloor/', views.EveryFloorView.as_view()),  # 统计每层人数占比





    # path('room/', views.RoomView.as_view),

]
# DRF框架的路由定义
router = DefaultRouter()  # 定义可以处理视图的路由器
router.register(r'room', views.RoomView, basename='房屋')  # 向路由器中注册视图集，并起别名
router.register(r'people', views.PeopleView, basename='人员')  # 向路由器中注册视图集，并起别名
router.register(r'RentDetails', views.RentDetailsView, basename='RentDetails')  # 向路由器中注册视图集，并起别名
router.register(r'RepairReport', views.RepairReportView, basename='RepairReport')  # 向路由器中注册视图集，并起别名
router.register(r'WaterElectricity', views.WaterElectricityView, basename='WaterElectricity')  # 向路由器中注册视图集，并起别名
router.register(r'DeviceDetail', views.DeviceDetailView, basename='DeviceDetail')  # 设备管理
router.register(r'BuildName', views.BuildNameView, basename='BuildName')  # 楼名
router.register(r'Floor', views.FloorView, basename='Floor')  # 楼层
router.register(r'RoomType', views.RoomTypeView, basename='RoomType')  # 房屋类型
router.register(r'RoomCategory', views.RoomCategoryView, basename='RoomCategory')  # 房屋类别
router.register(r'Department', views.DepartmentView, basename='Department')  # 部门
router.register(r'BedNumber', views.BedNumberView, basename='BedNumber')  # 床号
router.register(r'User', views.UserView, basename='User')  # 用户
router.register(r'RoomNumber', views.RoomNumberView, basename='RoomNumber')  # 房间号
router.register(r'DeviceList', views.DeviceListView, basename='DeviceList')  # 设备清单
router.register(r'Payment', views.PaymentView, basename='Payment')  # 充值房租
router.register(r'Deduction', views.DeductionView, basename='Deduction')  # 扣款
router.register(r'PeopleName', views.PeopleNameView, basename='PeopleName')  # 用户姓名
router.register(r'PaymentWaterElectricity', views.PaymentWaterElectricityView,
                basename='PaymentWaterElectricity')  # 水电费充值
router.register(r'DeductionWaterElectricity', views.DeductionWaterElectricityView,
                basename='DeductionWaterElectricity')  # 扣水电费
router.register(r'CheckInRecord', views.CheckInRecordView, basename='CheckInRecord')  # 入住记录


# router.register(r'peoples', views.PeoplesView, basename='peoples')  # 向路由器中注册视图集，并起别名
urlpatterns += router.urls  # 将路由器中的所有路由信息追加到Django的路由列表（urlpatterns）中
