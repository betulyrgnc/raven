# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 13:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Canceled')], default=0, verbose_name='Status')),
                ('subject', models.TextField(verbose_name='Subject')),
                ('start_date', models.DateTimeField(verbose_name='Start Date')),
                ('end_date', models.DateTimeField(verbose_name='End Date')),
                ('appointee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL, verbose_name='Appointee')),
                ('created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created')),
            ],
            options={
                'verbose_name_plural': 'Appointments',
                'verbose_name': 'Appointment',
            },
        ),
    ]
