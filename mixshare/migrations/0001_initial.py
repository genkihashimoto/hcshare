# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('like', models.IntegerField()),
                ('play', models.IntegerField()),
                ('repost', models.IntegerField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('registed_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
