# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-18 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_im', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=500, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=15, verbose_name='标题'),
        ),
    ]
