import os

from graphics.models import Group


def absoluteUrl(request):
    '''Returns absolute site root '''

    separ = os.sep
    domen_url_list = request.build_absolute_uri().split(separ)
    domen_url_path = domen_url_list[0] + separ + separ + domen_url_list[2]

    return {'DOMEN_URL': domen_url_path}


def listGroups(request):
    return {'GROUPS_LIST': Group.objects.all()}
