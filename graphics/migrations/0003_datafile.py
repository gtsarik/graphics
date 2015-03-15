# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphics', '0002_auto_20150313_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_path', models.FileField(upload_to=b'', null=True, verbose_name='\u0414\u0430\u043d\u043d\u044b\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u0424\u0430\u0439\u043b \u0434\u043b\u044f \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430',
                'verbose_name_plural': '\u0424\u0430\u0439\u043b\u044b \u0434\u043b\u044f \u043f\u0430\u0440\u0441\u0438\u043d\u0433\u0430',
            },
            bases=(models.Model,),
        ),
    ]
