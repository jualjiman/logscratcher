# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scratcher', '0006_auto_20150128_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='last_update',
            field=models.DateTimeField(help_text=b'Fecha y hora de inicio de la publicacion', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='server',
            name='password',
            field=models.CharField(help_text=b"Server pass for user, not needed if you're in authoriced_keys ", max_length=30),
            preserve_default=True,
        ),
    ]
