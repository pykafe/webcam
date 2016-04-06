# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 00:46
from __future__ import unicode_literals

from django.db import migrations
import webcam.fields
import webcam.storage


class Migration(migrations.Migration):

    dependencies = [
        ('webcamapp', '0008_auto_20160406_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoperson',
            name='picture',
            field=webcam.fields.CameraField(blank=True, null=True, storage=webcam.storage.CameraStorage(), upload_to='staticimages', verbose_name='Please upload Photo'),
        ),
    ]