# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-07-13 13:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0009_auto_20200713_1351'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]