from django.urls import path
from .views import AdmissionCreateView

app_name = 'admissions'
urlpatterns = [
    path('', AdmissionCreateView.as_view(), name='enquiry'),
]
