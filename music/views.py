from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Album, Band, Playlist


def home_page(request):
    current_user = request.user
    playlists = Playlist.objects.filter(created_by=current_user).count()
    albums = Album.objects.filter(created_by=current_user).count()
    bands = Band.objects.filter(created_by=current_user).count()

    context = {
        'playlists': playlists,
        'albums': albums,
        'bands': bands,
    }

    return render(request, 'music/home.html', context)


''' Band Views '''


class BandListView(ListView):
    model = Band
    template_name = "music/band_list.html"

    # Get only bands created by the current user
    def get_queryset(self, **kwargs):
        qs = Band.objects.filter(created_by=self.request.user)
        return qs


''' Album Views '''


class AlbumListView(ListView):
    model = Album
    template_name = "music/album_list.html"

    # Get only bands created by the current user
    def get_queryset(self, **kwargs):
        qs = Album.objects.filter(created_by=self.request.user)
        return qs


''' Playlists Views '''


class PlaylistListView(ListView):
    model = Playlist
    template_name = "music/playlist_list.html"

    # Get only bands created by the current user
    def get_queryset(self, **kwargs):
        qs = Playlist.objects.filter(created_by=self.request.user)
        return qs


class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'music/playlist_detail.html'


def delete_playlist(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    # playlist.delete()
    data = {
        'status': 200,
        'msg': 'Playlist deleted successfully'
    }
    return JsonResponse(data)
