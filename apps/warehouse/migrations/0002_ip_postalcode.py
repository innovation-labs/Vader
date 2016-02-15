# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipstore',
            name='postal_code',
            field=models.OneToOneField(null=True, blank=True, to='cities.PostalCode'),
        ),
    ]
