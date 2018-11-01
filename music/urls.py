from django.urls import path

from .views import home_page, AlbumListView, BandListView, PlaylistListView

urlpatterns = [
    path('', home_page, name="home"),
    path('album_list/', AlbumListView.as_view(), name="album-list"),
    path('band_list/', BandListView.as_view(), name="band-list"),
    path('playlist_list/', PlaylistListView.as_view(), name="playlist-list"),
]
