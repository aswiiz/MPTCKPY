from django.contrib import admin
from .models import Faculty

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'designation')
    list_filter = ('department', 'designation')
    search_fields = ('name', 'email')
