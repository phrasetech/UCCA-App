# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-08 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uccaApp', '0009_categories_is_metacategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='cluster',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]