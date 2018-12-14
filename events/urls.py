# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views, apis


urlpatterns = [
    # API Views
    # ex: /events/api/v1/list
    url(r'^api/v1/list$', apis.list_events_api, name='list_events_api'),

    # WEB Views
    # ex: /events/delete [POST]
    url(r'^delete/(?P<event_id>[0-9]+)$',
        views.delete_event_view, name='delete_event_view'),
]
