# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-11-05 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0003_auto_20181105_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='fecha_rescate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
