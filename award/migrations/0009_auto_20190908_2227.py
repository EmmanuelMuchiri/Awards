# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-08 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0008_subscribers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='profile',
            new_name='profile_id',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='project',
            new_name='project_id',
        ),
    ]
