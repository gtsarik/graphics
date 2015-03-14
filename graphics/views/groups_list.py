from django.shortcuts import render
from django.http import HttpResponse

def groupsList(request):
    return render(request, 'groups_list.html', {})

