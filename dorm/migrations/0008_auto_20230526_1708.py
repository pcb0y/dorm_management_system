# Generated by Django 3.2.15 on 2023-05-26 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0007_auto_20230526_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentdetails',
            name='payee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.user', verbose_name='收款人'),
        ),
        migrations.AlterField(
            model_name='rentdetails',
            name='people',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.people', verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='rentdetails',
            name='rent_price',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.rent', verbose_name='租金单价'),
        ),
        migrations.AlterField(
            model_name='repairreport',
            name='repair_device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.devicelist', verbose_name='维修设备'),
        ),
        migrations.AlterField(
            model_name='repairreport',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.room', verbose_name='房间号'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RoomCategory', to='dorm.roomcategory', verbose_name='房屋类别'),
        ),
    ]
