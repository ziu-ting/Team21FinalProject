# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170608_0717'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mood',
        ),
    ]
