from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'is_active')
    list_filter = ('is_active', 'date_posted')
    search_fields = ('title', 'content')
