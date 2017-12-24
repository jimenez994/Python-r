# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-17 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_app', '0005_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_author',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book_author',
            name='book',
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='belt_app.Book'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='book_author',
        ),
    ]