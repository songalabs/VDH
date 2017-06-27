# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-20 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vdh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='supervising_vet',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.SET_DEFAULT, to='vdh.Vet'),
        ),
    ]
