# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-07-13 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0010_auto_20200713_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='presenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='archive.Presenter'),
        ),
    ]
