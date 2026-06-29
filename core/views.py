from django.views.generic import TemplateView
from django.urls import reverse
from .models import Notice
from .site_data import DEPARTMENTS, GALLERY_CATEGORIES, UPDATED_SOON, local_media_images

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['depts'] = [{**dept, 'url': reverse(dept['route'])} for dept in DEPARTMENTS]
        ctx['facilities'] = [
            {'icon': 'bi bi-pc-display-horizontal', 'name': 'Smart Computer Labs'},
            {'icon': 'bi bi-motherboard', 'name': 'Electronics Labs'},
            {'icon': 'bi bi-hdd-rack', 'name': 'Hardware Labs'},
            {'icon': 'bi bi-book', 'name': 'Central Library'},
            {'icon': 'bi bi-projector', 'name': 'Seminar Hall'},
            {'icon': 'bi bi-camera-video', 'name': 'Smart Classrooms'},
            {'icon': 'bi bi-person-walking', 'name': 'Sports Facilities'},
            {'icon': 'bi bi-wifi', 'name': 'High-Speed Internet'},
        ]
        ctx['gallery_preview'] = local_media_images(limit=8)
        ctx['gallery_categories'] = GALLERY_CATEGORIES
        ctx['updated_soon'] = UPDATED_SOON
        return ctx


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['updated_soon'] = UPDATED_SOON
        return ctx


class ContactView(TemplateView):
    template_name = 'core/contact.html'
