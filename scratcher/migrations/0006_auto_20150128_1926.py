# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scratcher', '0005_project_server'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='data',
        ),
        migrations.AddField(
            model_name='server',
            name='host',
            field=models.CharField(default='host', help_text=b'Server host', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='password',
            field=models.CharField(default='password', help_text=b'Server pass for user', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='user',
            field=models.CharField(default='user', help_text=b'Server user', max_length=30),
            preserve_default=False,
        ),
    ]
