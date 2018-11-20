from django.urls import include, path

from .views import home_page, AlbumListView, BandListView, PlaylistDetailView, PlaylistListView, delete_playlist

urlpatterns = [
    path('', home_page, name="home"),
    path('album_list/', AlbumListView.as_view(), name="album-list"),
    path('band_list/', BandListView.as_view(), name="band-list"),
    path('playlist/', include([
        path('list/', PlaylistListView.as_view(), name="playlist-list"),
        path('detail/<int:pk>', PlaylistDetailView.as_view(), name="playlist-detail"),
        path('delete/<int:pk>', delete_playlist, name="playlist-detail")
    ])),
]
