# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20161018_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
