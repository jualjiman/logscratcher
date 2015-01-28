# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scratcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='last_update',
            field=models.DateTimeField(help_text=b'Fecha y hora de inicio de la publicacion', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(help_text=b'Project status', max_length=30, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
