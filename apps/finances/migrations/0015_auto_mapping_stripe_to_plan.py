# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0014_mapping_stripe_on_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='duration',
            new_name='interval',
        ),
    ]
