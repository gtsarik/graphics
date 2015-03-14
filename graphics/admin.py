# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from .models import Group, Parameter

class GroupAdmin(admin.ModelAdmin):
    pass

class ParameterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Group, GroupAdmin)
admin.site.register(Parameter, ParameterAdmin)
