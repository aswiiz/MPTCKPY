from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'established_year', 'hod_name')
    search_fields = ('name', 'code')
