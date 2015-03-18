# -*- coding: utf-8 -*-
from django.db import models


class Parameter(models.Model):
    ''' Parameter Model'''

    class Meta(object):
        verbose_name = u"Параметр"
        verbose_name_plural = u"Параметры"

    name = models.CharField(
        max_length=255,
        blank=False,
        unique=True,
        verbose_name=u"Название")

    def __unicode__(self):
        return u"%s" % (self.name)
