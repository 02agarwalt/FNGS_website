# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='collection_site',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
    ]