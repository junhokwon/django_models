# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_models', '0007_auto_20170605_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_models.Manufacturer'),
        ),
    ]
