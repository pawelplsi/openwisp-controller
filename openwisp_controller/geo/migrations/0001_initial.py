# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 15:19
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('openwisp_users', '0001_initial'),
        ('config', '0009_device_system'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceLocation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(choices=[('outdoor', 'Outdoor'), ('indoor', 'Indoor'), ('mobile', 'Mobile')], max_length=8)),
                ('indoor', models.CharField(blank=True, max_length=64, null=True, verbose_name='indoor position')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='config.Device')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FloorPlan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('floor', models.SmallIntegerField(verbose_name='floor')),
                ('image', models.ImageField(help_text='floor plan image', upload_to='', verbose_name='image')),
                ('name', models.CharField(blank=True, max_length=32, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=75, unique=True, verbose_name='name')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='address')),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326, verbose_name='geometry')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='floorplan',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.Location'),
        ),
        migrations.AddField(
            model_name='floorplan',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization'),
        ),
        migrations.AddField(
            model_name='devicelocation',
            name='floorplan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo.FloorPlan'),
        ),
        migrations.AddField(
            model_name='devicelocation',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo.Location'),
        ),
    ]
