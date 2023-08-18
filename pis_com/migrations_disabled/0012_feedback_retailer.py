# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-02-07 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pis_retailer', '0004_auto_20180623_1526'),
        ('pis_com', '0011_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='retailer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retailer_feedback', to='pis_retailer.Retailer'),
        ),
    ]