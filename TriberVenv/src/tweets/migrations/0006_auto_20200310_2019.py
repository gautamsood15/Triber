# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2020-03-10 20:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20200301_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-timestamp']},
        ),
    ]
