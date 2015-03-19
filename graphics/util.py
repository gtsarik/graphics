# -*- coding: utf-8 -*-


def get_groups(request):
    """Returns list of existing groups"""
    # deferred import of Group model to avoid cycled imports
    from .models import Group

    # get currently selected group
    cur_group = get_current_group(request)
    groups = []

    for group in Group.objects.all().order_by('region'):
        groups.append({
            'id': group.id,
            'region': group.region,
            'selected': cur_group and cur_group.id == group.id and True or False
        })

    return groups


def get_parameters(request):
    """Returns list of existing paarmeters"""
    # deferred import of Group model to avoid cycled imports
    from .models import Parameter

    # get currently selected group
    cur_param = get_current_param(request)
    parameters = []

    for parameter in Parameter.objects.all().order_by('name'):
        parameters.append({
            'id': parameter.id,
            'name': parameter.name,
            'selected': cur_param and cur_param.id == parameter.id
            and True or False
        })

    return parameters


def get_current_group(request):
    """Returns currently selected group or None"""

    # we remember selected group in a cookie
    pk = request.COOKIES.get('current_group')

    if pk:
        from .models import Group
        try:
            group = Group.objects.get(pk=int(pk))
        except Group.DoesNotExist:
            return None
        else:
            return group
    else:
        return None


def get_current_param(request):
    """Returns currently selected parameter of group or None"""

    # we remember selected parameter in a cookie
    pk = request.COOKIES.get('current_param')

    if pk:
        from .models import Parameter
        try:
            parameter = Parameter.objects.get(pk=int(pk))
        except Parameter.DoesNotExist:
            return None
        else:
            return parameter
    else:
        return None
