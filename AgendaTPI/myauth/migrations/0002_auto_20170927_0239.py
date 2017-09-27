# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='extra_info',
            field=models.CharField(max_length=100),
        ),
    ]
