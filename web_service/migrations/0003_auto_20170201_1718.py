# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_service', '0002_auto_20170201_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='web_service_level',
            options={'verbose_name': 'Web Service Level'},
        ),
    ]