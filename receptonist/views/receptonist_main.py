

# Generic View Class
from django.views.generic import TemplateView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from receptonist.permissions import ReceptonistPassesTestMixin



class ReceptonistHomeView(LoginRequiredMixin, ReceptonistPassesTestMixin, TemplateView):
    template_name = 'receptonist/receptonist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Receptonist"
        return context
    