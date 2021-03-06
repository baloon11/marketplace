# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 15:34
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='title')),
                ('text', ckeditor.fields.RichTextField(verbose_name='text')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('ordering', models.IntegerField(default=100, verbose_name='ordering')),
            ],
            options={
                'verbose_name': 'help article',
                'verbose_name_plural': 'help',
                'ordering': ['ordering'],
            },
        ),
    ]
