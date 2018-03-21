from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Album
from .models import Songs

# Create your views here.


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = Songs.objects.filter(album=album).all()
    context = {
        'album': album,
        'songs': songs
    }
    return render(request, 'music/detail.html', context)
