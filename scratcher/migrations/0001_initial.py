# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Project Name', max_length=100, blank=True)),
                ('path', models.CharField(help_text=b'Project Path', max_length=300, blank=True)),
                ('status', models.CharField(help_text=b'Ruta del proyecto', max_length=30, blank=True)),
                ('last_update', models.DateTimeField(help_text=b'Fecha y hora de inicio de la publicacion', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
