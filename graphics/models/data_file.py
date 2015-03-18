# -*- coding: utf-8 -*-
from django.db import models


class DataFile(models.Model):
    ''' Data File Model'''

    class Meta(object):
        verbose_name = u"Файл для парсинга"
        verbose_name_plural = u"Файлы для парсинга"

    file_path = models.FileField(
        blank=True,
        verbose_name=u"Данные",
        null=True)

    def __unicode__(self):
        return u"%s" % (self.file_path)
