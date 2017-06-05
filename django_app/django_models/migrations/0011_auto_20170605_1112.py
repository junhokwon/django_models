# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_models', '0010_auto_20170605_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='person_type',
        ),
        migrations.RemoveField(
            model_name='person',
            name='shirt_size',
        ),
        migrations.RemoveField(
            model_name='person',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='django_models.Membership', to='django_models.Person'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_models.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.DeleteModel(
            name='Persons',
        ),
    ]