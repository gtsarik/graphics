# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError
import csv
import os

from .models import Group, Parameter, DataFile


class GroupAdmin(admin.ModelAdmin):
    ''' Admin for Group Model '''

    list_display = ['region']
    list_display_links = ['region']
    ordering = ['region']
    list_filter = ['region']
    list_per_page = 10
    search_fields = ['region']

class ParameterAdmin(admin.ModelAdmin):
    ''' Admin for Parameter Model '''

    list_display = ['groups', 'param', 'name', 'value']
    list_display_links = ['param', 'name', 'groups']
    list_editable = ['value']
    ordering = ['param']
    list_filter = ['param', 'groups', 'name']
    list_per_page = 10
    search_fields = ['groups', 'param', 'name', 'value']

class DataFileFormAdmin(ModelForm):
    ''' Form for DataFile Admin '''

    def clean(self):
        ''' Check file extension. '''

        extension = str(self.cleaned_data['file_path'])

        if not extension.endswith('.csv'):
            raise ValidationError(u'Файл должен быть с расширением .csv',
                code='invalid')

        return self.cleaned_data

class DataFileAdmin(admin.ModelAdmin):
    ''' Admin for DataFile Model '''

    list_display = ['file_path']
    actions = ['csv_parsing_write_db', 'delete_file']
    form = DataFileFormAdmin


    # Creating these steps to remove the file (s) from the database and server
    def delete_file(self, request, queryset):
        from graphicsapp.settings import MEDIA_ROOT

        file_list = []

        for qs in queryset:
            file_name = str(qs.file_path)[2:]
            file_path = os.path.join(MEDIA_ROOT, file_name)
            qs.delete()
            os.remove(file_path)
            file_list.append(file_name)

        if len(file_list) == 1:
            self.message_user(request, u"Файл %s удален." % (file_name))
        else:
            self.message_user(request, u"Файлы %s удалены." % (file_list))

    # Adding a name for the action to delete a file (s) from the database and server
    delete_file.short_description = "Удалить выбраные файлы из базы и с сервера"


    # Create an action of the parser and write to the database
    # in the admin panel for the model parameters
    def csv_parsing_write_db(self, request, queryset):
        from graphicsapp.settings import MEDIA_ROOT

        # Number listed to and updated parameters in the database
        upadate_bit = 0
        create_bit = 0
        
        # We pass on the list of chosen files
        for qs in queryset:
            file_name = str(qs.file_path)[2:]
            file_path = os.path.join(MEDIA_ROOT, file_name)

            try:
                # Open csv file
                with open(file_path) as csvfile:
                    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')

                    # Get the list of groups and remove empty elements
                    group = next(csvreader)
                    group = filter(str.strip, group)

                    # Get the list of parameters without line groups
                    next(csvreader)

                    # We pass through the list of parameters
                    for row in csvreader:
                        count = 0
                        row = filter(str.strip, row)
                        parameter = ':'.join(row)
                        parameter = parameter.split(':')
                        size_parameter = len(parameter) - 1

                        while (count < size_parameter):
                            # Write the name of the group in the database
                            # if it does not exist in the database
                            region = Group.objects.get_or_create(region=parameter[0])[0]

                            # If the parameter already exists, its value is updated
                            # otherwise, write
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
                                create_bit += 1
                            count += 2
            except Exception:
                pass
        # Display a message on the listed to or updated data
        self.message_user(request, u"%d параметров обновлено и %d параметров добавлено." % (upadate_bit, create_bit))

    # Add the name of the parser and write to the database
    # in the admin panel for the model Parameters
    csv_parsing_write_db.short_description = "Добавить данные в базу"


admin.site.register(Group, GroupAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(DataFile, DataFileAdmin)
