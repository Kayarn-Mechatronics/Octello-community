# Generated by Django 3.2.5 on 2021-09-08 01:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceApp', '0006_auto_20210908_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountscategories',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 1, 49, 48, 532063)),
        ),
        migrations.AlterModelTable(
            name='accounts',
            table='FinanceApp_Accounts',
        ),
    ]
