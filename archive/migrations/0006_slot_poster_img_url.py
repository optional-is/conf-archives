# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-04 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_conference_attendees'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='poster_img_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
