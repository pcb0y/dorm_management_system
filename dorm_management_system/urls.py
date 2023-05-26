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
from django.urls import path
from dorm import views
from rest_framework.routers import DefaultRouter # 导入路由器定义的包

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('room/', views.RoomView.as_view),
]
# DRF框架的路由定义
router = DefaultRouter()  # 定义可以处理视图的路由器
router.register(r'room', views.RoomView, basename='房屋')  # 向路由器中注册视图集，并起别名
router.register(r'people', views.PeopleView, basename='人员')  # 向路由器中注册视图集，并起别名
router.register(r'RentDetails', views.RentDetailsView, basename='RentDetails')  # 向路由器中注册视图集，并起别名
router.register(r'RepairReport', views.RepairReportView, basename='RepairReport')  # 向路由器中注册视图集，并起别名
# router.register(r'peoples', views.PeoplesView, basename='peoples')  # 向路由器中注册视图集，并起别名
urlpatterns += router.urls  # 将路由器中的所有路由信息追加到Django的路由列表（urlpatterns）中
