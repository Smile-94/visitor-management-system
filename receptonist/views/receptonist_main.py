import datetime

# Generic View Class
from django.views.generic import TemplateView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from receptonist.permissions import ReceptonistPassesTestMixin

# Models
from appointment.models import AppointmentApplication



class ReceptonistHomeView(LoginRequiredMixin, ReceptonistPassesTestMixin, TemplateView):
    template_name = 'receptonist/receptonist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Receptonist"
        context["appointment_today"] = AppointmentApplication.objects.filter(appointment_of__appointment_date=datetime.date.today(),accept_status=True).count()
        context["not_issued"] = AppointmentApplication.objects.filter(appointment_of__appointment_date=datetime.date.today(),accept_status=True,issued_status=False).count()
        context["issued"] = AppointmentApplication.objects.filter(appointment_of__appointment_date=datetime.date.today(),accept_status=True,issued_status=True).count()
        return context
    