# -*- coding: utf-8 -*-
# from django.shortcuts import render
from ..util import get_current_group, get_current_param
import json
from django.views.generic.base import TemplateView
from django.http import JsonResponse

from ..models import Value


class GroupListView(TemplateView):
    template_name = 'groups_list.html'

    def get_context_data(self, **kwargs):
        ''' View for graphic page '''
        context = super(GroupListView, self).get_context_data(**kwargs)

        context['current_group'] = get_current_group(self.request)
        context['current_param'] = get_current_param(self.request)

        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        chart_dict = {}
        chart_data = []

        try:
            group_id = data['group_id']
            param_id = data['param_id']

            # Get a list of all values in the group and parameter
            values = Value.objects.filter(
                groups_id=group_id,
                parameters_id=param_id)

            for value in values:
                chart_dict['parameter'] = value.name.encode('utf-8')
                chart_dict['value'] = value.value
                chart_data.append(chart_dict)
                chart_dict = {}
        except Exception:
            pass

        chart_data = json.dumps(chart_data)

        return JsonResponse({'data': chart_data})
