# Generated by Django 3.2.5 on 2021-09-06 16:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AssetsApp', '0004_auto_20210906_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetscategories',
            name='user',
            field=models.ForeignKey(default='OCAUTHUSR-1', on_delete=django.db.models.deletion.CASCADE, to='AuthenticationApp.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assetscategories',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 16, 14, 16, 974889)),
        ),
    ]
