# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-09 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spot', '0002_auto_20180409_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asg',
            name='refreshed_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]