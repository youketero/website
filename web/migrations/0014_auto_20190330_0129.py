# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-29 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_partner_hyper_link_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='cathed',
            name='email',
            field=models.TextField(default='http'),
        ),
        migrations.AddField(
            model_name='cathed',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]