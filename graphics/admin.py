# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
# from django.forms import ModelForm, ValidationError
import csv

from .models import Group, Parameter, DataFile



class GroupAdmin(admin.ModelAdmin):
    pass

class ParameterAdmin(admin.ModelAdmin):
    pass

class DataFileAdmin(admin.ModelAdmin):
    list_display = ['file_path']
    actions = ['csv_parsing_write_db', 'delete_file']

    def delete_file(self, request, queryset):
        if queryset:
            for n in queryset:
                n.delete()
    delete_file.short_description = "Удалить выбраные файлы"

    def csv_parsing_write_db(self, request, queryset):
        from ..grahicsapp.settings import FILEPATH
        # print '=== request ===', request
        print '=== queryset ===', queryset[0].file_path

        # with open('2CuNPefD.csv', 'rw') as csvfile:
        # csvreader = csv.reader(csvfile, delimiter=',', quotechar='\n')
        # qw = next(csvreader)
        # qw = filter(str.strip, qw)
        # # print len(qw)
        # next(csvreader)

        # for row in csvreader:
        #     row = filter(str.strip, row)
        #     st = ':'.join(row)
        #     new = st.split(':')

        #     # print len(new)
        #     # print new

        #     for m in xrange(len(new)):
        #         print qw[m]
        #         print new[m]
        #     print  '*********************************************'

    csv_parsing_write_db.short_description = "Добавить данные в базу"


admin.site.register(Group, GroupAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(DataFile, DataFileAdmin)
