# -*- coding: utf-8 -*-
from .util import get_groups, get_parameters


def groupsProcessor(request):
    return {'GROUPS': get_groups(request)}


def parametersProcessor(request):
    return {'PARAMETERS': get_parameters(request)}
