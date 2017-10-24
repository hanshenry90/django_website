from django.conf.urls import url
from . import views

app_name ='music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'), # request nothing ^$

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), # 'detail' is the url request pattern: r'^(?P<album_id>[0-9]+)/$', now go find your response in views.detail
    # /music/<album_id>/favoite
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')

    # /music/album/add/    ...a form generated
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add')
]