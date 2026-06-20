from django.views.generic import ListView
from .models import Faculty

class FacultyListView(ListView):
    model = Faculty
    template_name = 'faculty/faculty_list.html'
    context_object_name = 'faculties'
    
    def get_queryset(self):
        return Faculty.objects.select_related('department').all()
