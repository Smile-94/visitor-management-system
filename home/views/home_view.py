

# Generic View Class
from django.views.generic import TemplateView


class HomveView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home" 
        return context
    