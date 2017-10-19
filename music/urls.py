from django.conf.urls import url
from . import views

app_name ='music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'), # request nothing ^$

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), # 'detail' is the url request pattern: r'^(?P<album_id>[0-9]+)/$', now go find your response in views.detail
]