# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_popularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularity',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]
