# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-14 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baselaunch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationVersionCloudConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_instance_type', models.CharField(blank=True, max_length=256, null=True)),
                ('default_launch_config', models.TextField(blank=True, help_text='Instance Initial configuration data to parameterize the launch.', max_length=16384, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='application',
            name='frontend_component_name',
        ),
        migrations.RemoveField(
            model_name='application',
            name='frontend_component_path',
        ),
        migrations.RemoveField(
            model_name='applicationversion',
            name='images',
        ),
        migrations.RemoveField(
            model_name='applicationversion',
            name='launch_data',
        ),
        migrations.AddField(
            model_name='applicationversion',
            name='backend_component_name',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='applicationversion',
            name='frontend_component_name',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='applicationversion',
            name='frontend_component_path',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='applicationversioncloudconfig',
            name='application_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_version', to='baselaunch.ApplicationVersion'),
        ),
        migrations.AddField(
            model_name='applicationversioncloudconfig',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='baselaunch.CloudImage'),
        ),
        migrations.AlterUniqueTogether(
            name='applicationversioncloudconfig',
            unique_together=set([('application_version', 'image')]),
        ),
    ]
