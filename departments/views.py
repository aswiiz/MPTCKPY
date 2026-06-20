from django.views.generic import TemplateView

class DepartmentListView(TemplateView):
    template_name = 'departments/department_list.html'

class ComputerEngineeringView(TemplateView):
    template_name = 'departments/ce.html'

class ComputerHardwareEngineeringView(TemplateView):
    template_name = 'departments/che.html'

class ElectronicsEngineeringView(TemplateView):
    template_name = 'departments/ee.html'

class ElectronicsCommunicationView(TemplateView):
    template_name = 'departments/ece.html'

class ElectricalElectronicsView(TemplateView):
    template_name = 'departments/eee.html'
