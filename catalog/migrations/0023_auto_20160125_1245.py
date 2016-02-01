# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20160120_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='browser_title',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='browser title'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='meta description'),
        ),
        migrations.AddField(
            model_name='item',
            name='browser_title',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='browser title'),
        ),
        migrations.AddField(
            model_name='item',
            name='meta_description',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='meta description'),
        ),
    ]