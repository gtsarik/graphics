# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError
import csv
import os

from .models import Group, Parameter, DataFile


class GroupAdmin(admin.ModelAdmin):
    list_display = ['region']
    list_display_links = ['region']
    ordering = ['region']
    list_filter = ['region']
    list_per_page = 10
    search_fields = ['region']

class ParameterAdmin(admin.ModelAdmin):
    list_display = ['groups', 'param', 'name', 'value']
    list_display_links = ['param', 'name', 'groups']
    list_editable = ['value']
    ordering = ['param']
    list_filter = ['param', 'groups', 'name']
    list_per_page = 10
    search_fields = ['groups', 'param', 'name', 'value']

class DataFileFormAdmin(ModelForm):
    def clean(self):
        """Check ifile_extension."""

        extension = str(self.cleaned_data['file_path'])

        if not extension.endswith('.csv'):
            raise ValidationError(u'Файл должен быть с расширением .csv',
                code='invalid')

        return self.cleaned_data

class DataFileAdmin(admin.ModelAdmin):
    list_display = ['file_path']
    actions = ['csv_parsing_write_db', 'delete_file']
    form = DataFileFormAdmin

    def delete_file(self, request, queryset):
        if queryset:
            for n in queryset:
                n.delete()
    delete_file.short_description = "Удалить выбраные файлы"

    def csv_parsing_write_db(self, request, queryset):
        from graphicsapp.settings import MEDIA_ROOT
        upadate_bit = 0
        create_bit = 0
        
        for qs in queryset:
            file_name = str(qs.file_path)[2:]
            file_path = os.path.join(MEDIA_ROOT, file_name)

            try:
                with open(file_path) as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    group = next(csvreader)
                    group = filter(str.strip, group)
                    next(csvreader)

                    for row in csvreader:
                        count = 0
                        row = filter(str.strip, row)
                        parameter = ':'.join(row)
                        parameter = parameter.split(':')
                        size_parameter = len(parameter) - 1

                        while (count < size_parameter):
                            # print '=== COUNT === ', count
                            region = Group.objects.get_or_create(region=parameter[0])[0]

                            if Parameter.objects.filter(param=group[count+1], name=parameter[count+1], groups_id=region.id).exists():
                                param = Parameter.objects.filter(param=group[count+1],
                                    name=parameter[count+1],
                                    groups_id=region.id).update(value=parameter[count+2])
                                upadate_bit += 1
                            else:
                                param = Parameter.objects.create(param=group[count+1],
                                    name=parameter[count+1],
                                    groups_id=region.id,
                                    value=parameter[count+2])
                                create_bit = 1
                            count += 2
            except Exception:
                pass
        self.message_user(request, u"%d параметров обновлено и %d параметров добавлено." % (upadate_bit, create_bit))
    csv_parsing_write_db.short_description = "Добавить данные в базу"


admin.site.register(Group, GroupAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(DataFile, DataFileAdmin)
