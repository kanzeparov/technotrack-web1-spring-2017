# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_blog_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]