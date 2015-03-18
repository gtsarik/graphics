# -*- coding: utf-8 -*-
from django.db import models


class Value(models.Model):
    ''' Value Model'''

    class Meta(object):
        verbose_name = u"Значение"
        verbose_name_plural = u"Значения"

    name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name=u"Название")

    value = models.IntegerField(
        blank=False,
        default=0,
        verbose_name=u"Значение")

    parameters = models.ForeignKey(
        'Parameter',
        blank=False,
        verbose_name=u"Параметр",
        on_delete=models.PROTECT)

    groups = models.ForeignKey(
        'Group',
        blank=False,
        verbose_name=u"Область",
        on_delete=models.PROTECT)

    def __unicode__(self):
        return u"%s %s" % (self.parameters.name, self.name, self.value)
