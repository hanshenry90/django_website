# from django.http import HttpResponse
from django.http import Http404
# from django.template import loader
from django.shortcuts import render
from . models import Album

def index(request): # views function

    all_albums=Album.objects.all()
    # template = loader.get_template('music/index.html') # Provides templates to views.py
    context = {
        'all_albums': all_albums # A dictionary of the Album objects in database that the template needs to work behinde scene
    }
    return render(request, 'music/index.html', context) # A built in HttpResponse in render()

    # html=''
    # for i in all_albums:
    #     url='/music/' + str(i.id) + '/'
    #     html += '<a href="' + url + '">' + i.album_title + '</a><br>'
    # return HttpResponse(template.render(context, request)) # Give the response to user's request in url

def detail(request, album_id):

    # return HttpResponse("<h2>Detailes for Album id: " + str(album_id) + "</h2>")
    try:
        album=Album.objects.get(pk=album_id)

    except Album.DoesNotExist:
        raise Http404("Album does not exist!")
    return render(request, 'music/detail.html', {'cao':album})
