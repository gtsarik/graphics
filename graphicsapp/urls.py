from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Groups List Url
    url(r'^$', 'graphics.views.groups_list.groupsList', name='home'),

    # Admin Url
    url(r'^admin/', include(admin.site.urls)),
)
