# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 18:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20170313_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='utr',
        ),
    ]
