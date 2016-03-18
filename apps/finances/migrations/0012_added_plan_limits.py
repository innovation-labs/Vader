# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0011_module_segment'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='limit_campaigns',
            field=models.IntegerField(default=0, help_text=b'0 means unlimited'),
        ),
        migrations.AddField(
            model_name='plan',
            name='limit_impressions',
            field=models.IntegerField(default=0, help_text=b'0 means unlimited'),
        ),
        migrations.AddField(
            model_name='plan',
            name='modules',
            field=models.ManyToManyField(through='finances.PlanModule', to='finances.Module'),
        ),
    ]