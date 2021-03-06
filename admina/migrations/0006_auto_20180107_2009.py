# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admina', '0005_auto_20171215_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='IsUse',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='apply',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01db610-f3a3-11e7-a2d9-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01e0430-f3a3-11e7-9aa3-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='creation',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01d40de-f3a3-11e7-a200-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='creation2projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01d67f0-f3a3-11e7-ae59-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01e2b40-f3a3-11e7-960b-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='helpapplication',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01e7961-f3a3-11e7-883f-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01ddd1f-f3a3-11e7-9826-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='messagetype',
            name='Uuid',
            field=models.URLField(blank=True, default=b'a01ddd1e-f3a3-11e7-bfb3-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='praise',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01db60f-f3a3-11e7-90ab-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01ccbae-f3a3-11e7-92c4-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='project2projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01cf2c0-f3a3-11e7-9c2f-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01ccbaf-f3a3-11e7-b474-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01d19d0-f3a3-11e7-9428-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01d8f00-f3a3-11e7-9376-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01e2b41-f3a3-11e7-b8fc-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01e524f-f3a3-11e7-a86d-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='scorechange',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01e5250-f3a3-11e7-868c-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01ca49e-f3a3-11e7-96a9-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='user2userlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01d19cf-f3a3-11e7-94c3-002324d72502', null=True),
        ),
        migrations.AlterField(
            model_name='userlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a01cf2c1-f3a3-11e7-a0a8-002324d72502', null=True),
        ),
    ]
