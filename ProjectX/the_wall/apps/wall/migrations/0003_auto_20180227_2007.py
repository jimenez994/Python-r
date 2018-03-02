# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-27 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_auto_20180227_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='wall.User'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_by', to='wall.User'),
        ),
    ]