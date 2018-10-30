from django.contrib import admin
from .models import Album, Band


admin.site.register(Album)

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    exclude = ('created_by', )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()