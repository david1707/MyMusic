from django.contrib import admin
from .models import Album, Band, Playlist


class BandAdmin(admin.ModelAdmin):
    include = ('name', 'created_by')
    list_display = ('name', 'created_by')
    list_filter = ('created_by',)
    ordering = ('name',)
    search_fields = ('name',)

admin.site.register(Band, BandAdmin)


class AlbumAdmin(admin.ModelAdmin):
    include = ('band_name', 'album_name', 'published_year','edition_year','bought_year','price','country','state_condition', 'observations','created_by',)
    list_display = ('album_name', 'band_name', 'published_year','edition_year','bought_year','price','country','state_condition', 'created_by',)
    list_filter = ('created_by', )
    ordering = ('album_name', 'band_name', 'bought_year')
    search_fields = ('album_name',)

admin.site.register(Album, AlbumAdmin)


class PlaylistAdmin(admin.ModelAdmin):
    include = ('name', 'albums', 'publish', 'publish_accepted', 'created_by')
    list_display = ('name', 'get_total_albums', 'publish', 'publish_accepted', 'created_by')
    list_filter = ('created_by',)
    ordering = ('name',)
    search_fields = ('name',)

    def get_total_albums(self, obj):
        total_albums = len(obj.albums.all())
        return total_albums

    get_total_albums.short_description = "Total albums"
    


admin.site.register(Playlist, PlaylistAdmin)