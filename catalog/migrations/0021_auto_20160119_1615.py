# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_category_sku_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsku',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dictionary.Color', verbose_name='color'),
            preserve_default=False,
        ),
    ]
