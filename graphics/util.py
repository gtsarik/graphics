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
