# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0001_initial'),
        ('Contratos', '0007_contrato_costo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='Cuenta',
            field=models.ForeignKey(default='1234567890', on_delete=django.db.models.deletion.CASCADE, to='Cuentas.Cuenta'),
            preserve_default=False,
        ),
    ]
