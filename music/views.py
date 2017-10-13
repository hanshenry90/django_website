from django.http import HttpResponse

def index(request): # views function
    return HttpResponse("<h1>My Music<h1>")
