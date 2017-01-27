# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-24 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='Date Created')),
            ],
        ),
    ]
