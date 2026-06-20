from django.views.generic import TemplateView

class PlacementsView(TemplateView):
    template_name = 'placements/placements.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['companies'] = [
            'TCS', 'Infosys', 'Wipro', 'Cognizant', 'Tech Mahindra',
            'L&T Infotech', 'UST Global', 'IBS Software', 'Mphasis',
            'KELTRON', 'BEL', 'BSNL', 'NIC', 'KSEB',
        ]
        return ctx
