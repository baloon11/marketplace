# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20160112_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='fabric',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='fabric structure'),
        ),
    ]
