from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # django looks for pattern that match url
    url(r'^music/', include('music.urls')) # the request of music url has a response: music/urls.py, include(file.py)
]
