from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Album

class IndexView(generic.ListView): # inherent from type ListView
    template_name='music/index.html'
    context_object_name='all_albums' # override object_list

    def get_queryset(self):         # query the dataset
        return Album.objects.all()  # return as a object_list

class DetailView(generic.DetailView):
    model=Album # what model/databaseObject are you trying to get details of?
    template_name='music/detail.html' # HttpResponse

# Generating a Model form, inherent from CreateView Class
class AlbumCreate(CreateView):
    model=Album
    fields=['artist', 'album_title', 'genre', 'album_logo'] # field is an object used in templates


# from django.http import HttpResponse
# from django.http import Http404
# from django.template import loader
# from django.shortcuts import render, get_object_or_404
# from . models import Album


# def index(request): # views function
#
#     all_albums=Album.objects.all()
#     # template = loader.get_template('music/index.html') # Provides templates to views.py
#     context = {
#         'all_albums': all_albums # A dictionary of the Album objects in database that the template needs to work behinde scene
#     }
#     return render(request, 'music/index.html', context) # A built in HttpResponse in render()
#
#     # html=''
#     # for i in all_albums:
#     #     url='/music/' + str(i.id) + '/'
#     #     html += '<a href="' + url + '">' + i.album_title + '</a><br>'
#     # return HttpResponse(template.render(context, request)) # Give the response to user's request in url
#
# def detail(request, album_id):
#
#     # return HttpResponse("<h2>Detailes for Album id: " + str(album_id) + "</h2>")
#     # try:
#     #     album=Album.objects.get(pk=album_id)
#     #
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist!")
#
#     album=get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album':album}) # model access, album class in return
#
# def favorite(request, album_id):
#     album=get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song=album.song_set.get(pk=request.POST['song'])
#     except (KeyError, song.DoesNotExist):
#         return(request, 'music/detail.html', {'album':album,
#                                               'error_message':"You did not select a valid song."})
#
#     else:
#         selected_song.is_favorite=True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album':album})

