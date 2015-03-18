# -*- coding: utf-8 -*-
from django.shortcuts import render
from ..util import get_current_group, get_current_param

# from ..models import Group, Parameter


def groupsList(request):
    ''' View for graphic page '''

    current_group = get_current_group(request)
    current_param = get_current_param(request)

    return render(
        request,
        'groups_list.html',
        {'CURRENT_PARAMETERS': current_param,
        'CURRENT_GROUP': current_group}
    )
