# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2024-02-16 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dating_sex', models.CharField(choices=[('男', '男'), ('女', '女')], default='女', max_length=8, verbose_name='性别的匹配')),
                ('location', models.CharField(max_length=32, verbose_name='目标城市')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最小查找目标')),
                ('max_distance', models.IntegerField(default=10, verbose_name='最大查找目标')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最小交友范围')),
                ('max_dating_age', models.IntegerField(default=45, verbose_name='最大交友范围')),
                ('vibration', models.BooleanField(default=True, verbose_name='是否开启震动')),
                ('only_matche', models.BooleanField(default=True, verbose_name='不让为匹配的人看我的相册')),
                ('auto_play', models.BooleanField(default=True, verbose_name='是否自动播放视频')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=32, unique=True)),
                ('phonenum', models.CharField(max_length=16, unique=True)),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=8)),
                ('avatar', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=32)),
                ('birth_year', models.IntegerField()),
                ('birth_month', models.IntegerField()),
                ('birth_day', models.IntegerField()),
            ],
        ),
    ]
