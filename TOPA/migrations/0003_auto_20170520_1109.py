# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOPA', '0002_flight_passengers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date',
            field=models.DateField(),
        ),
    ]
