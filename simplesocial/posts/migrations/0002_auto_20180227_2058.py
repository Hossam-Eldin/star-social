# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-27 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='message_html',
        ),
        migrations.AddField(
            model_name='post',
            name='messages_html',
            field=models.TextField(default='post'),
        ),
    ]
