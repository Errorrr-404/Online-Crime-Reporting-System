# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('case', '0001_initial'),
        ('citizen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='citizen.Citizen'),
        ),
    ]