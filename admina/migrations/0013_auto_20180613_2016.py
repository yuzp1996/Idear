# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-13 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admina', '0012_auto_20180613_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='ScoreRankName',
        ),
        migrations.AlterField(
            model_name='apply',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b47730-6f03-11e8-820d-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b4ec61-6f03-11e8-b99e-68f728892930', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='creation',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b3daf0-6f03-11e8-b689-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='creation2projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b40200-6f03-11e8-a2c1-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b51370-6f03-11e8-8128-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='helpapplication',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b5afb0-6f03-11e8-a666-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b4c54f-6f03-11e8-8d39-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='messagetype',
            name='Uuid',
            field=models.URLField(blank=True, default=b'a6b49e40-6f03-11e8-b6fa-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='praise',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b4501e-6f03-11e8-82f9-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b3179e-6f03-11e8-aaf5-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='project2projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b365c0-6f03-11e8-84fe-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b33eae-6f03-11e8-961b-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b3b3de-6f03-11e8-8db2-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b4290f-6f03-11e8-a1a6-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b53a80-6f03-11e8-99e2-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b56191-6f03-11e8-96dc-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='scorechange',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b588a1-6f03-11e8-a9da-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b2c980-6f03-11e8-8500-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='user2userlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b38cd0-6f03-11e8-8886-68f728892930', null=True),
        ),
        migrations.AlterField(
            model_name='userlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=b'a6b38ccf-6f03-11e8-8a0d-68f728892930', null=True),
        ),
    ]