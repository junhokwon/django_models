# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_models', '0020_lecture3_student3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student3',
            name='student3',
        ),
        migrations.DeleteModel(
            name='Lecture3',
        ),
        migrations.DeleteModel(
            name='Student3',
        ),
    ]