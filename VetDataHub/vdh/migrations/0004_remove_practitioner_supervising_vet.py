# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-20 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vdh', '0003_auto_20170420_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practitioner',
            name='supervising_vet',
        ),
    ]
