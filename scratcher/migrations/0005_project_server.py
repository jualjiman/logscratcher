# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scratcher', '0004_auto_20150128_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='server',
            field=models.ForeignKey(default=1, to='scratcher.Server'),
            preserve_default=False,
        ),
    ]
