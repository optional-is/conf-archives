# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-07-13 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0011_auto_20200713_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='transcript',
            field=models.TextField(blank=True, null=True),
        ),
    ]
