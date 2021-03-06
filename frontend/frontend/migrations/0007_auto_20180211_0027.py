# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-11 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_feed_owner'),
    ]

    operations = [
        migrations.RunSQL("ALTER TABLE `frontend_feed` ADD COLUMN `js` ENUM('Y','N') DEFAULT 'N' NOT NULL;"
                          "ALTER TABLE `frontend_feed` ALTER COLUMN `js` DROP DEFAULT;",
                          state_operations=[
                              migrations.AddField(
                                model_name='feed',
                                name='js',
                                field=models.CharField(choices=[(b'N', b'No javascript'), (b'Y', b'With javascript')], default=b'N', max_length=1),
                              )
                          ]),
        migrations.AddField(
            model_name='feed',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
