from django.views.generic import ListView
from .models import Gallery

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'images'
    ordering = ['-date_added']
