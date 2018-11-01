from django.shortcuts import render

from .models import Album, Band, MyPlaylist


def home_page(request):
    return render(request, 'music/home.html')