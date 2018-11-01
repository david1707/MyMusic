from django.contrib import admin
from .models import Album, Band, Playlist


admin.site.register(Album)
admin.site.register(Playlist)

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    include = '__all__'
    # exclude = ('created_by', )

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.created_by = request.user
    #     obj.save()