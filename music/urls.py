from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index') # .index is the function name that views.py applies to； ^$ end of url, home section
]