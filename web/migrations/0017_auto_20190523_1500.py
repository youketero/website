# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-23 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20190331_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.TextField(default='sername'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.TextField(default='name'),
        ),
    ]
