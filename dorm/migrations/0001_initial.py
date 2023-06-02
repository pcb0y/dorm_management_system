# Generated by Django 3.2.15 on 2023-05-30 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BedNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_name', models.CharField(max_length=10, verbose_name='床号')),
            ],
            options={
                'verbose_name': '床号表',
                'verbose_name_plural': '床号表',
            },
        ),
        migrations.CreateModel(
            name='BuildName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_name', models.CharField(max_length=30, null=True, verbose_name='楼名')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=20, verbose_name='部门名称')),
            ],
            options={
                'verbose_name': '部门信息表',
                'verbose_name_plural': '部门信息表',
            },
        ),
        migrations.CreateModel(
            name='DeviceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=20, null=True, verbose_name='设备名称')),
                ('device_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='设备价格')),
            ],
            options={
                'verbose_name': '设备清单表',
                'verbose_name_plural': '设备清单表',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('sex', models.SmallIntegerField(verbose_name='性别')),
                ('phone', models.CharField(max_length=11, verbose_name='手机')),
                ('people_number', models.CharField(max_length=18, verbose_name='身份证号')),
                ('check_in_time', models.DateField(verbose_name='入住时间')),
                ('check_out_time', models.DateField(null=True, verbose_name='退房时间')),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='押金')),
                ('remark', models.CharField(max_length=11, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('bed_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.bednumber', verbose_name='床号')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.department', verbose_name='关联部门表')),
            ],
            options={
                'verbose_name': '人员信息表',
                'verbose_name_plural': '人员信息表',
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='租金单价')),
            ],
            options={
                'verbose_name': '租金分类表',
                'verbose_name_plural': '租金分类表',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.CharField(max_length=10, verbose_name='楼层')),
                ('room_number', models.CharField(max_length=10, verbose_name='房间号')),
                ('number_of_people', models.SmallIntegerField(verbose_name='入住人数')),
                ('standard_number_of_people', models.SmallIntegerField(verbose_name='配标人数')),
                ('empty_bed_number', models.SmallIntegerField(verbose_name='空床数')),
                ('is_used', models.BooleanField(default=True, verbose_name='是否启用')),
                ('build_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.buildname', verbose_name='楼名')),
                ('device_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.devicelist', verbose_name='设备清单')),
            ],
            options={
                'verbose_name': '房屋信息表',
                'verbose_name_plural': '房屋信息表',
            },
        ),
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_Category_name', models.CharField(max_length=20, null=True, verbose_name='房屋类别')),
            ],
            options={
                'verbose_name': '房屋类别表',
                'verbose_name_plural': '房屋类别表',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20, verbose_name='房屋类型')),
            ],
            options={
                'verbose_name': '房屋类型表',
                'verbose_name_plural': '房屋类型表',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('power', models.SmallIntegerField(verbose_name='权限')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.CreateModel(
            name='WaterElectricity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mouth', models.CharField(max_length=6, verbose_name='年月数')),
                ('start_water_code', models.DecimalField(decimal_places=1, max_digits=20, verbose_name='水费表码起')),
                ('end_water_code', models.DecimalField(decimal_places=1, max_digits=20, verbose_name='水费表码止')),
                ('water_sum', models.DecimalField(decimal_places=1, max_digits=20, verbose_name='水表数')),
                ('water_price', models.DecimalField(decimal_places=2, default=1, max_digits=20, verbose_name='水费单价')),
                ('water_amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='水费金额')),
                ('water_time', models.DateTimeField(verbose_name='水费抄表时间')),
                ('start_electricity_code', models.DecimalField(decimal_places=1, max_digits=20, verbose_name='电表表码起')),
                ('end_electricity_code', models.DecimalField(decimal_places=1, max_digits=20, verbose_name='电表表码止')),
                ('electricity_sum', models.DecimalField(decimal_places=1, max_digits=20, verbose_name='电表数')),
                ('electricity_price', models.DecimalField(decimal_places=2, default=1.2, max_digits=20, verbose_name='电费单价')),
                ('electricity_amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='电费金额')),
                ('electricity_time', models.DateTimeField(verbose_name='电费抄表时间')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.room', verbose_name='房间编码')),
            ],
            options={
                'verbose_name': '水电费明细表',
                'verbose_name_plural': '水电费明细表',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='room_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.roomcategory', verbose_name='房屋类别'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.roomtype', verbose_name='房屋类型'),
        ),
        migrations.CreateModel(
            name='RepairReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_time', models.DateTimeField(verbose_name='报修日期')),
                ('fault_description', models.CharField(max_length=50, null=True, verbose_name='故障说明')),
                ('is_quality_guarantee_period', models.BooleanField(null=True, verbose_name='是否保质期内')),
                ('repair_cost', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='维修费用')),
                ('is_self_cost', models.BooleanField(null=True, verbose_name='是否自费')),
                ('repair_people', models.CharField(max_length=10, null=True, verbose_name='维修人')),
                ('is_repaired', models.BooleanField(default=False, verbose_name='是否修好')),
                ('repair_date', models.DateField(verbose_name='修复日期')),
                ('remark', models.CharField(max_length=100, null=True, verbose_name='备注')),
                ('people', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.people', verbose_name='报修人')),
                ('repair_device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.devicelist', verbose_name='维修设备')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.room', verbose_name='房间号')),
            ],
            options={
                'verbose_name': '维修明细表',
                'verbose_name_plural': '维修明细表',
            },
        ),
        migrations.CreateModel(
            name='RentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mouth', models.CharField(max_length=6, verbose_name='年月数')),
                ('payable_amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='应缴金额')),
                ('actual_amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='实缴金额')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='余额')),
                ('payment_date', models.DateTimeField(verbose_name='缴费时间')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
                ('payee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.user', verbose_name='收款人')),
                ('people', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.people', verbose_name='姓名')),
                ('rent_price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.rent', verbose_name='租金单价')),
            ],
            options={
                'verbose_name': '租金明细表',
                'verbose_name_plural': '租金明细表',
            },
        ),
        migrations.AddField(
            model_name='people',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_name', to='dorm.room', verbose_name='房间号'),
        ),
        migrations.AddField(
            model_name='people',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.user', verbose_name='录入人'),
        ),
        migrations.CreateModel(
            name='DeviceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_number', models.IntegerField(default=1, verbose_name='设备数量')),
                ('remark', models.CharField(max_length=50, null=True, verbose_name='备注')),
                ('device_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.devicelist', verbose_name='设备名称')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.room', verbose_name='房间号')),
            ],
            options={
                'verbose_name': '设备详情表',
                'verbose_name_plural': '设备详情表',
            },
        ),
    ]
