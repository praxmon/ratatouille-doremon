# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-14 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratatouille', '0008_menuitems_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.IntegerField(null=True)),
                ('count', models.IntegerField(null=True)),
                ('pre', models.IntegerField(null=True)),
                ('errorCode', models.IntegerField()),
                ('asr_text', models.CharField(blank=True, max_length=255, null=True)),
                ('nlu_text', models.CharField(blank=True, max_length=255, null=True)),
                ('asr_time', models.CharField(blank=True, max_length=255, null=True)),
                ('nlu_time', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
