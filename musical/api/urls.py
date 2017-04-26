from django.conf.urls import include, url
from django.contrib import admin
from .views import (GenreListAPI,
    GenreDetailAPI,
    GenreUpdateAPI,
    GenreDestroyAPI,
    MusicDetailAPI,
    MusicUpdateAPI,
    MusicDestroyAPI,
    MusicListAPI,MusicCreateAPI,GenreCreateAPI)



urlpatterns = [
    url(r'^(?P<pk>\d+)/edit$',GenreUpdateAPI.as_view(),name='api_update'),
    url(r'^(?P<pk>\d+)/$',GenreDetailAPI.as_view(),name='api_detail'),
    url(r'^create/$',GenreCreateAPI.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/delete/$',GenreDestroyAPI.as_view(),name='api_delete'),
    url(r'^$',GenreListAPI.as_view(),name='api_list'),

    url(r'^(?P<pk>\d+)/update$',MusicUpdateAPI.as_view(),name='api_music_update'),
    url(r'^(?P<pk>\d+)/list$',MusicDetailAPI.as_view(),name='api_music_detail'),
    url(r'^(?P<pk>\d+)/remove/$',MusicDestroyAPI.as_view(),name='api_music_delete'),
    url(r'^show/$',MusicListAPI.as_view(),name='api_music_list'),
    url(r'^music_create/$',MusicCreateAPI.as_view(),name='music_create')

    # url(r'^music_edit/(?P<id>\d+)/$',music_update,name='music_update'),
    # url(r'^(?P<id>\d+)/$',music_detail,name='music_detail'),

    # url(r'^(?P<id>\d+)/music_delete/$',music_delete,name='music_delete'),
    # url(r'^list/$',music_list,name='music_list')

    
]
