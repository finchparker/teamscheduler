# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-05 13:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamcode', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('kakao_id', models.CharField(max_length=60)),
            ],
        ),
    ]