# Generated by Django 2.1.5 on 2019-10-10 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0042_auto_20191010_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_list',
            name='current',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
