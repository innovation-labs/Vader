# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-10 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0017_plan_stripe_id'),
        ('companies', '0022_auto_20160309_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True)),
                ('updated_on', django_extensions.db.fields.ModificationDateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('stripe_id', models.CharField(max_length=256)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='companies.Company')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='finances.Plan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]