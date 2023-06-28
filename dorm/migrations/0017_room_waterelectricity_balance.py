# Generated by Django 3.2.15 on 2023-06-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0016_paymentwaterelectricity'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='WaterElectricity_Balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, null=True, verbose_name='水电费余额'),
        ),
    ]