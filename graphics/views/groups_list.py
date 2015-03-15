from django.shortcuts import render
import csv
from django.http import HttpResponse

from ..models import Group, Parameter


def groupsList(request):
    return render(request, 'groups_list.html', {})

