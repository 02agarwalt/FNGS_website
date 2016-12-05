# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_id', models.CharField(max_length=30)),
                ('collection_site', models.CharField(max_length=40)),
                ('output_url', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.CharField(max_length=30)),
                ('struct_scan', models.FileField(upload_to=b'')),
                ('func_scan', models.FileField(upload_to=b'')),
                ('output_url', models.CharField(blank=True, max_length=200, null=True)),
                ('slice_timing', models.CharField(choices=[(None, 'None'), ('up', 'Bottom Up Acquisition (standard)'), ('down', 'Top Down Acquisition'), ('interleaved', 'Interleaved Acquisition')], max_length=20)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyze.Dataset')),
            ],
        ),
    ]
