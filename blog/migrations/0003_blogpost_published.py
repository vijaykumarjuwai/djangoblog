# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170713_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
