# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_service', '0002_auto_20170213_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='web_service',
            options={'ordering': ['name'], 'verbose_name': 'Web Service'},
        ),
        migrations.AlterModelOptions(
            name='web_service_level',
            options={'ordering': ['level'], 'verbose_name': 'Web Service Level'},
        ),
        migrations.AlterField(
            model_name='web_service',
            name='actual_url',
            field=models.CharField(help_text='Full URL of layer / web service that includes the actual machine name and port of host machine that ArcGIS Server (which creates/contains the web services) resides.  Note that if only one layer is defined in the web service then put the full URL including the index number of that layer.  Else, include no index numbers Eg. https://kens-arcgis-001-prod:6443/arcgis/rest/services/PVS/Long_Trails_Structures_WSE/MapServer/0', max_length=150),
        ),
        migrations.AlterField(
            model_name='web_service',
            name='location',
            field=models.CharField(help_text='https://kens-arcgis-001-prod:6443/arcgis/rest/services/PVS/Long_Trails_Structures_WSE/MapServer/0', max_length=50),
        ),
    ]
