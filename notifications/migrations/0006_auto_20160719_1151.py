# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_auto_20160718_2334'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Tokens',
        ),
    ]
