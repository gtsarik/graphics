# -*- coding: utf-8 -*-
from django.shortcuts import render
# from django.http import HttpResponse

from ..models import Group, Parameter



def groupsList(request):
    ''' View for graphic page '''
    return render(request, 'groups_list.html', {})


