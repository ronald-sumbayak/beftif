# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 22:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170930_0828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
    ]
