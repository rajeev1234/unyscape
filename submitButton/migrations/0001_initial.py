# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2021-07-10 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input1', models.CharField(max_length=200)),
                ('input2', models.CharField(max_length=200)),
            ],
        ),
    ]
