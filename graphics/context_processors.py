# -*- coding: utf-8 -*-
from .util import get_groups


def groupsProcessor(request):
    return {'GROUPS': get_groups(request)}
