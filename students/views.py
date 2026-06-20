from django.views.generic import TemplateView

class StudentPortalView(TemplateView):
    template_name = 'students/portal.html'
