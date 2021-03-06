# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 15:50
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_shop_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='shop',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='description'),
        ),
    ]
