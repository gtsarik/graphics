# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='param',
        ),
        migrations.AlterField(
            model_name='parameter',
            name='value',
            field=models.IntegerField(default=0, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]
