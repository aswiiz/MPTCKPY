from django.contrib import admin
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('title',)
