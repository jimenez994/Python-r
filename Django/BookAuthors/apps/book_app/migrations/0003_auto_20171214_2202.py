# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_author_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_author',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_app.Author'),
        ),
    ]
