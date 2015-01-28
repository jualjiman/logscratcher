# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scratcher', '0003_server'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='serverName',
            new_name='name',
        ),
    ]
