from django.http import HttpResponse

def index(request): # views function
    return HttpResponse("<h1>Music</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Detailes for Album id: " + str(album_id) + "</h2>")

