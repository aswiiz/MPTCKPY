from django.views.generic import TemplateView
from core.site_data import RECRUITERS, PLACEMENT_STATS


class PlacementsView(TemplateView):
    template_name = 'placements/placements.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Use only verified official data
        ctx['companies'] = RECRUITERS
        ctx['stats'] = PLACEMENT_STATS
        ctx['recent_drives'] = []  # No fake drives — leave empty until real data is added
        return ctx
