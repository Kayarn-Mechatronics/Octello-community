# Generated by Django 3.2.5 on 2021-09-08 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetsApp', '0012_alter_assetscategories_datetime_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetscategories',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 2, 36, 18, 493735)),
        ),
    ]
