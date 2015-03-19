# -*- coding: utf-8 -*-
from django.contrib import admin
# from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError
import csv
import os

from .models import Group, Parameter, DataFile, Value


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

    list_display = ['name']
    list_display_links = ['name']
    ordering = ['name']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']


class ValueAdmin(admin.ModelAdmin):
    ''' Admin for Value Model '''

    list_display = ['groups', 'parameters', 'name', 'value']
    list_display_links = ['parameters', 'name', 'groups']
    list_editable = ['value']
    ordering = ['parameters']
    list_filter = ['parameters', 'groups', 'name']
    list_per_page = 10
    search_fields = ['groups', 'parameters', 'name', 'value']


class DataFileFormAdmin(ModelForm):
    ''' Form for DataFile Admin '''

    def clean(self):
        ''' Check file extension. '''

        extension = str(self.cleaned_data['file_path'])

        if not extension.endswith('.csv'):
            raise ValidationError(
                u'Файл должен быть с расширением .csv',
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

    # Adding a name for the action to delete a file(s)
    # from the database and server
    delete_file.short_description = u"Удалить выбраные файлы из базы и с сервера"

    # Create an action of the parser and write to the database
    # in the admin panel for the model parameters
    def csv_parsing_write_db(self, request, queryset):
        from graphicsapp.settings import MEDIA_ROOT

        # Number listed to and updated parameters in the database
        upadate_bit = 0
        create_bit = 0

        # We pass on the list of chosen files
        for qs in queryset:
            # csv_file_path = ''
            # data = []
            file_name = str(qs.file_path)[2:]
            file_path = os.path.join(MEDIA_ROOT, file_name)

            try:
                # Open csv file
                with open(file_path) as csvfile:
                    csvreader = csv.reader(
                        csvfile,
                        delimiter=',',
                        quotechar='|')

                    # Get the list of groups and remove empty elements
                    group = next(csvreader)
                    group = filter(str.strip, group)

                    # Get the list of parameters without line groups
                    # next(csvreader)

                    # We pass through the list of parameters
                    for row in csvreader:
                        count = 0
                        row = filter(str.strip, row)
                        param = ':'.join(row)
                        param = param.split(':')
                        size_parameter = len(param) - 1

                        region = Group.objects.get_or_create(
                                region=param[0])[0]

                        while (count < size_parameter):
                            # Write the name of the group in the database
                            # if it does not exist in the database

                            parameter = Parameter.objects.get_or_create(
                                name=group[count+1])[0]

                            # print '=== while ==='
                            # id_region = region.id
                            # id_parameter = parameter.id
                            # csv_file_name = str(id_region) + '_' + str(id_parameter) + '.csv'
                            # csv_file_path = os.path.join(folder_path, csv_file_name)

                            # print '=== csv_file_path === ', csv_file_path

                            # If the parameter already exists,
                            # its value is updated otherwise, write
                            if Value.objects.filter(
                                    name=param[count+1],
                                    parameters_id=parameter.id,
                                    groups_id=region.id).exists():
                                value = Value.objects.filter(
                                    name=param[count+1],
                                    parameters_id=parameter.id,
                                    groups_id=region.id).update(
                                        value=param[count+2])
                                upadate_bit += 1
                            else:
                                value = Value.objects.create(
                                    name=param[count+1],
                                    parameters_id=parameter.id,
                                    groups_id=region.id,
                                    value=param[count+2])
                                create_bit += 1
                            # line = param[count+1] + ',' + param[count+2]
                            # data.append(line)

                            # print '=== line === ', line
                            # print '=== region === ', param[0]
                            # print '=== param === ', group[count+1]
                            # print '=== value === ', param[count+2]

                            # print '**********************************************'

                            count += 2
                    # print '=== DATA === ', data

                    # with open(csv_file_path, "w+") as f:
                    #     for n in data:
                    #         f.write(n)
            except Exception, e:
                # pass
                print 'ERROR: %s' % e

        self.csv_write_file()

        # Display a message on the listed to or updated data
        self.message_user(
            request,
            u"%d параметров обновлено и %d параметров добавлено." %
            (upadate_bit, create_bit))

    # Add the name of the parser and write to the database
    # in the admin panel for the model Parameters
    csv_parsing_write_db.short_description = "Добавить данные в базу"

    def csv_write_file(self):
        folder_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'static/json'))

        try:
            groups = Group.objects.all()
            parameters = Parameter.objects.all()

            for group in groups:
                id_group = group.id

                for parameter in parameters:
                    id_parameter = parameter.id
                    csv_file_name = str(id_group) + '_' + str(id_parameter) + '.csv'
                    csv_file_path = os.path.join(folder_path, csv_file_name)

                    try:
                        ofile = open(csv_file_path, "wb")
                        print '=== OPEN ==='
                        writer = csv.writer(ofile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        print '=== writer ==='
                        values = Value.objects.filter(
                            groups_id=id_group,
                            parameters_id=id_parameter)
                        print '=== values ==='

                        for value in values:
                            writer.writerow((value.name.encode('utf-8'), str(value.value)))
                            # row = '128'
                            # writer.writerow(row)
                    finally:
                        ofile.close()
        except Exception, e:
            print 'ERROR === %s' % e


admin.site.register(Group, GroupAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(DataFile, DataFileAdmin)
admin.site.register(Value, ValueAdmin)
