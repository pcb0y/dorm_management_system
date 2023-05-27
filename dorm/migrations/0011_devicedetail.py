# Generated by Django 3.2.15 on 2023-05-27 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0010_people_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_number', models.IntegerField(verbose_name='设备数量')),
                ('remark', models.CharField(max_length=50, verbose_name='备注')),
                ('device_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.devicelist', verbose_name='设备名称')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.room', verbose_name='房间号')),
            ],
        ),
    ]
