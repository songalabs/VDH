# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-20 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdh', '0019_auto_20170420_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practitioner',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='vet',
            name='profile_picture',
        ),
    ]