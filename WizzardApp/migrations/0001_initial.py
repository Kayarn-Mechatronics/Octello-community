# Generated by Django 3.2.5 on 2021-09-06 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WizzardsDB',
            fields=[
                ('wizzard_id', models.SmallIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80, unique=True)),
                ('description', models.TextField(max_length=100)),
                ('author', models.CharField(max_length=40)),
                ('source', models.CharField(max_length=40)),
                ('requests', models.PositiveIntegerField()),
                ('rating', models.PositiveIntegerField()),
                ('created', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
                ('verified', models.BooleanField(default=False)),
                ('verification_token', models.UUIDField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WizzardRatting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_id', models.PositiveBigIntegerField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('user_id', models.CharField(max_length=50, null=True, unique=True)),
                ('date_stamp', models.DateField()),
                ('time_stamp', models.TimeField()),
                ('wizzard_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WizzardApp.wizzardsdb')),
            ],
        ),
        migrations.CreateModel(
            name='WizzardComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commend_id', models.PositiveBigIntegerField(unique=True)),
                ('user_id', models.CharField(max_length=50)),
                ('comment_text', models.TextField()),
                ('date_stamp', models.DateField()),
                ('time_stamp', models.TimeField()),
                ('last_update', models.DateTimeField()),
                ('wizzard_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WizzardApp.wizzardsdb')),
            ],
        ),
    ]
