from django.urls import path
from .views import PlacementsView

app_name = 'placements'
urlpatterns = [
    path('', PlacementsView.as_view(), name='list'),
]
