# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 08:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mxd', '0003_auto_20170214_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mxd',
            options={'ordering': ['name'], 'verbose_name': 'MXD'},
        ),
        migrations.AlterModelOptions(
            name='mxd_client',
            options={'ordering': ['client'], 'verbose_name': 'MXD Client'},
        ),
        migrations.AlterModelOptions(
            name='mxd_creator',
            options={'ordering': ['creator'], 'verbose_name': 'MXD Creator'},
        ),
    ]
