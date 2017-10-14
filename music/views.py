from django.http import HttpResponse
from . models import Album

def index(request): # views function
    all_albums=Album.objects.all()
    html=''
    for i in all_albums:
        url='/music/' + str(i.id) + '/'
        html += '<a href="' + url + '">' + i.album_title + '</a><br>'
        # html += '<a href="' + url + '">' + str(i.id) + '</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>Detailes for Album id: " + str(album_id) + "</h2>")

