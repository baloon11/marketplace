# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_auto_20160105_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
    ]
