from django.urls import path
from .views import StudentPortalView

app_name = 'students'
urlpatterns = [
    path('', StudentPortalView.as_view(), name='portal'),
]
