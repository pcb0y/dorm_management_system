# Generated by Django 3.2.15 on 2023-06-10 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0010_alter_rentdetails_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_user',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='payment_user', to='dorm.user', verbose_name='扣费人'),
            preserve_default=False,
        ),
    ]
