# -*- coding: utf-8 -*-
from django.shortcuts import render
from ..util import get_current_group, get_current_param

# from django.utils import simplejson
import simplejson


def groupsList(request):
    ''' View for graphic page '''

    current_group = get_current_group(request)
    current_param = get_current_param(request)

    chartData = {'a': '4'}

    js_data = simplejson.dumps(chartData)

    print '=== js_data === ', js_data
    # render_template_to_response("my_template.html", {"my_data": js_data, …})

    return render(
        request,
        'groups_list.html',
        {'CURRENT_PARAMETERS': current_param,
        'CURRENT_GROUP': current_group,
        "my_data": chartData}
    )
