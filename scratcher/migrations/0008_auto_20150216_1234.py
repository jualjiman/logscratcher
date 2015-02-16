# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scratcher', '0007_auto_20150212_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhereIs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'where are files to back up', max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_update',
            field=models.DateTimeField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text=b'Project Name', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='path',
            field=models.CharField(help_text=b'Project Path', max_length=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='server',
            field=models.ForeignKey(help_text=b'where to scratch log', to='scratcher.Server'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server',
            name='description',
            field=models.CharField(help_text=b'Some server notes', max_length=b'600', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server',
            name='password',
            field=models.CharField(help_text=b"Server pass for user, not needed if you're in authoriced_keys ", max_length=30, blank=True),
            preserve_default=True,
        ),
    ]
