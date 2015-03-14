# -*- coding: utf-8 -*-
from django.db import models

class Parameter(models.Model):
    ''' Parameter Model'''

    class Meta(object):
        verbose_name = u"Параметр"
        verbose_name_plural = u"Параметры"

    param = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=u"Параметр")

    name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=u"Название")

    value = models.IntegerField(
        blank=False,
        default=0,
        verbose_name=u"Значение")

    groups = models.ForeignKey('Group',
        verbose_name=u"Область",
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s %s" % (self.param, self.name)
