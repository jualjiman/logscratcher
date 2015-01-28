# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scratcher', '0002_auto_20150127_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serverName', models.CharField(help_text=b'Server Name', max_length=20)),
                ('data', models.CharField(help_text=b'Server data', max_length=100)),
                ('description', models.CharField(help_text=b'Some server notes', max_length=b'600')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
