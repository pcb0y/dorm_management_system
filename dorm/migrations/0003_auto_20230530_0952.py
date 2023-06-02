# Generated by Django 3.2.15 on 2023-05-30 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0002_remove_room_floor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_name', models.CharField(max_length=10, null=True, verbose_name='楼层')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='floor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dorm.floor', verbose_name='楼层'),
        ),
    ]