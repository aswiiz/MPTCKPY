from django.urls import path
from .views import (
    DepartmentListView,
    ComputerEngineeringView,
    ComputerHardwareEngineeringView,
    ElectronicsEngineeringView,
    ElectronicsCommunicationView,
    ElectricalElectronicsView
)

app_name = 'departments'
urlpatterns = [
    path('', DepartmentListView.as_view(), name='list'),
    path('computer-engineering/', ComputerEngineeringView.as_view(), name='ce'),
    path('computer-hardware-engineering/', ComputerHardwareEngineeringView.as_view(), name='che'),
    path('electronics-engineering/', ElectronicsEngineeringView.as_view(), name='ee'),
    path('electronics-communication/', ElectronicsCommunicationView.as_view(), name='ece'),
    path('electrical-electronics/', ElectricalElectronicsView.as_view(), name='eee'),
]
