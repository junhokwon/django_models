# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_models', '0002_auto_20170605_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(default='bmw', max_length=40),
            preserve_default=False,
        ),
    ]
