# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scratcher', '0008_auto_20150216_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='whereIs',
            field=models.ForeignKey(default=1, blank=True, to='scratcher.WhereIs', help_text=b'where are files to back up'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='whereis',
            name='name',
            field=models.CharField(help_text=b'Where is name', max_length=30),
            preserve_default=True,
        ),
    ]
