# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-20 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20190208_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='rozklad',
            name='cource',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=10000),
        ),
    ]
