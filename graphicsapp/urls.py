from django.conf.urls import patterns, include, url
from django.contrib import admin

from .settings import MEDIA_ROOT, DEBUG
from graphics.views.groups_list import GroupListView

urlpatterns = patterns('',
    # Groups List Url
    # url(r'^$', 'graphics.views.groups_list.groupsList', name='home'),
    url(r'^$', GroupListView.as_view(), name='home'),

    # Admin Url
    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))
