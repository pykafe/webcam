# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcamapp', '0004_auto_20160405_2359'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='PhotoPerson',
        ),
    ]