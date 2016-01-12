# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_color'),
        ('catalog', '0011_itemcustomproperty'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dictionary.Color', verbose_name='color'),
        ),
    ]