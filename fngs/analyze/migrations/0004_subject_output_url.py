# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0003_auto_20161113_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='output_url',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
