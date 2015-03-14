# -*- coding: utf-8 -*-
from django.db import models

class Group(models.Model):
    ''' Group Model'''

    class Meta(object):
        verbose_name = u"Область"
        verbose_name_plural = u"Области"

    region = models.CharField(
        max_length=255,
        blank=False,
        unique=True,
        verbose_name=u"Область")

    # param = models.OneToOneField('Parameter',
    #     verbose_name=u"Параметр",
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL)

    def __unicode__(self):
        return u"%s" % (self.region)
