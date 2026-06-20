from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import AdmissionEnquiry

class AdmissionCreateView(CreateView):
    model = AdmissionEnquiry
    template_name = 'admissions/admission_form.html'
    fields = ['student_name', 'email', 'phone', 'course_interested', 'message']
    success_url = reverse_lazy('admissions:enquiry')

    def form_valid(self, form):
        messages.success(self.request, 'Your enquiry has been submitted successfully!')
        return super().form_valid(form)
