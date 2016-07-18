# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_token', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Zip Code')),
                ('notification_time', models.TimeField(blank=True, verbose_name='Notification Time')),
                ('location_latitude', models.FloatField(blank=True, null=True, verbose_name='Latitude')),
                ('location_longitude', models.FloatField(blank=True, null=True, verbose_name='Longtitude')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
        ),
    ]
