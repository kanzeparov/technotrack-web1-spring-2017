# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_remove_comment_utr'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]