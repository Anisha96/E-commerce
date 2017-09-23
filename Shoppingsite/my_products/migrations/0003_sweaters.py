# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_products', '0002_dresses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sweaters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.FileField(upload_to='images')),
            ],
        ),
    ]
