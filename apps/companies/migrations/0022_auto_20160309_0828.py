# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 08:28
from __future__ import unicode_literals

from django.db import migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0021_auto_20160201_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='payment_data',
            field=django_pgjson.fields.JsonField(blank=True, default={}, null=True),
        ),
    ]
