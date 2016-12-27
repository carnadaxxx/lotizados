# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=250)),
                ('ApellidoPaterno', models.CharField(max_length=250)),
                ('ApellidoMaterno', models.CharField(max_length=250)),
                ('FechaNacimiento', models.DateField()),
            ],
        ),
    ]
