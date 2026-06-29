from django.views.generic import TemplateView
from django.http import Http404
from django.urls import reverse

from core.site_data import DEPARTMENTS, UPDATED_SOON, get_department_by_slug, local_media_images

class DepartmentListView(TemplateView):
    template_name = 'departments/department_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['departments'] = [{**dept, 'url': reverse(dept['route'])} for dept in DEPARTMENTS]
        return ctx


class DepartmentDetailView(TemplateView):
    template_name = 'departments/department_detail.html'
    slug = None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        dept = get_department_by_slug(self.slug)
        if not dept:
            raise Http404("Department not found")
        ctx['department'] = dept
        ctx['departments'] = DEPARTMENTS
        ctx['gallery_preview'] = local_media_images(limit=6)
        ctx['updated_soon'] = UPDATED_SOON
        return ctx


class ComputerEngineeringView(DepartmentDetailView):
    slug = 'computer-engineering'


class ComputerHardwareEngineeringView(DepartmentDetailView):
    slug = 'computer-hardware-engineering'


class ElectronicsEngineeringView(DepartmentDetailView):
    slug = 'electronics-engineering'


class ElectronicsCommunicationView(DepartmentDetailView):
    slug = 'electronics-communication'


class ElectricalElectronicsView(DepartmentDetailView):
    slug = 'electrical-electronics'


class MechanicalEngineeringView(DepartmentDetailView):
    slug = 'mechanical-engineering'
