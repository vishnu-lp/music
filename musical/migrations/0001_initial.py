# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_title', models.CharField(max_length=50)),
                ('rating', models.IntegerField(db_index=True)),
                ('slug', models.SlugField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musical.Genre')),
            ],
        ),
    ]
