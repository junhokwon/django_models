# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_models', '0008_auto_20170605_0923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tradeinfo',
            old_name='date_leave',
            new_name='date_leaved',
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]