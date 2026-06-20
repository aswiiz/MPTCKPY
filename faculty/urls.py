from django.urls import path
from .views import FacultyListView
from .views_portal import FacultyPortalView

app_name = 'faculty'
urlpatterns = [
    path('', FacultyListView.as_view(), name='list'),
    path('portal/', FacultyPortalView.as_view(), name='portal'),
]
