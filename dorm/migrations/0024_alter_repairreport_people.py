# Generated by Django 3.2.15 on 2023-06-18 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0023_auto_20230618_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairreport',
            name='people',
            field=models.ForeignKey(default=16, on_delete=django.db.models.deletion.CASCADE, to='dorm.people', verbose_name='报修人'),
            preserve_default=False,
        ),
    ]
