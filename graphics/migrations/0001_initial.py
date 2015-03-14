# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(unique=True, max_length=255, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u043b\u0430\u0441\u0442\u044c',
                'verbose_name_plural': '\u041e\u0431\u043b\u0430\u0441\u0442\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('param', models.CharField(max_length=255, verbose_name='\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('value', models.IntegerField(verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='\u041e\u0431\u043b\u0430\u0441\u0442\u044c', to='graphics.Group', null=True)),
            ],
            options={
                'verbose_name': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440',
                'verbose_name_plural': '\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='group',
            name='param',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='graphics.Parameter', verbose_name='\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440'),
            preserve_default=True,
        ),
    ]
