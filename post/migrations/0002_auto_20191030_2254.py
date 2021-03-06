# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-30 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        ('user', '0001_initial'),
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserProfile'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gallery.Image'),
        ),
        migrations.AlterUniqueTogether(
            name='postview',
            unique_together=set([('post', 'date', 'ip')]),
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together=set([('post', 'user')]),
        ),
    ]
