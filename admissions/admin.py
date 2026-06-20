from django.contrib import admin
from .models import AdmissionEnquiry

@admin.register(AdmissionEnquiry)
class AdmissionEnquiryAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'course_interested', 'date_submitted', 'status')
    list_filter = ('status', 'course_interested', 'date_submitted')
    search_fields = ('student_name', 'email', 'phone')
