# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-19 19:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20190320_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cource',
            name='cathed_name',
        ),
        migrations.DeleteModel(
            name='cource',
        ),
    ]