# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-07 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('post', '0006_auto_20190207_2107'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together=set([('post', 'user')]),
        ),
    ]