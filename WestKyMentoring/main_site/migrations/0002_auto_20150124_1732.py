# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='event_worker',
            options={'verbose_name': 'Event Workers'},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='individual',
            name='ssn',
            field=models.CharField(max_length=9, null=True),
            preserve_default=True,
        ),
    ]
