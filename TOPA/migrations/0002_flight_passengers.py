# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TOPA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='passengers',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]