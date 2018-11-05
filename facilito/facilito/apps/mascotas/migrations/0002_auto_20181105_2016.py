# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-11-05 20:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='edad_aproximada',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mascota',
            name='fecha_rescate',
            field=models.DateField(default=datetime.datetime(2018, 11, 5, 20, 16, 39, 605157, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='mascota',
            name='sexo',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='nombre',
            field=models.CharField(default='', max_length=50),
        ),
    ]
