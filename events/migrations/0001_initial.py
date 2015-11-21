# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_event', models.CharField(max_length=100)),
                ('days', models.IntegerField(help_text=b'Days after which you should go to         the event')),
                ('msg_to_send', models.TextField()),
            ],
            options={
                'verbose_name': 'General Event',
            },
        ),
        migrations.CreateModel(
            name='ScheduledEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_event', models.CharField(max_length=100)),
                ('days', models.IntegerField(help_text=b'Minimum child age in days to be eligible to go to         the event')),
                ('event_date', models.DateField()),
                ('msg_to_send', models.TextField()),
            ],
            options={
                'verbose_name': 'Scheduled Event',
            },
        ),
    ]
