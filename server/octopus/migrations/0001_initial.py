# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-06-19 18:31
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
            name='Lightbulb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('item_no', models.CharField(max_length=6)),
                ('img', models.CharField(max_length=200)),
                ('wattage', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('brand', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('colour', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('performance200', models.IntegerField()),
                ('performance250', models.IntegerField()),
                ('performance300', models.IntegerField()),
                ('performance350', models.IntegerField()),
                ('performance400', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
