# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
