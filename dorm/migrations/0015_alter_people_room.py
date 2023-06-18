# Generated by Django 3.2.15 on 2023-06-17 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0014_alter_devicedetail_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='people', to='dorm.room', verbose_name='房间号'),
        ),
    ]
