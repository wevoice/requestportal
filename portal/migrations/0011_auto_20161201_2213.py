# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 22:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20161201_2210'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TSRequest',
            new_name='Request',
        ),
    ]
