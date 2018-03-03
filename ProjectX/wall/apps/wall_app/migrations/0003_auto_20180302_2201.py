# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-02 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0002_remove_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='wall_app.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall_app.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_by', to='wall_app.User'),
        ),
    ]
