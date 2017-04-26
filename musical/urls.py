from django.conf.urls import include, url
from django.contrib import admin
from musical.views import (genre_create,genre_detail,genre_list,
    genre_update,
    genre_delete,
    music_create,
    music_detail,
    music_list,
    music_update,
    music_delete)

urlpatterns = [
    url(r'^edit/(?P<id>\d+)/$',genre_update,name='update'),
    url(r'^(?P<id>\d+)/$',genre_detail,name='detail'),
    url(r'^create/$',genre_create,name='create'),
    url(r'^(?P<id>\d+)/delete/$',genre_delete,name='delete'),
    url(r'^$',genre_list,name='list'),
    url(r'^music_edit/(?P<id>\d+)/$',music_update,name='music_update'),
    url(r'^(?P<id>\d+)/show$',music_detail,name='music_detail'),
    url(r'^music_create/$',music_create,name='music_create'),
    url(r'^(?P<id>\d+)/music_delete/$',music_delete,name='music_delete'),
    url(r'^list/$',music_list,name='music_list')

    
]
