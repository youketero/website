# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]