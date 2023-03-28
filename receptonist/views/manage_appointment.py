
# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from receptonist.permissions import ReceptonistPassesTestMixin

# Generic Classes
from django.views.generic import ListView
from django.views.generic import DetailView

# Models
from appointment.models import AppointmentApplication

# Filter Classes 
from appointment.filters import PendingAppointmentApplicationFilter



class ReceptionAppointmentListView(LoginRequiredMixin, ReceptonistPassesTestMixin, ListView ):
    Model = AppointmentApplication
    queryset = AppointmentApplication.objects.filter(is_active=True, issued_status=False)
    filterset_class = PendingAppointmentApplicationFilter
    template_name = 'receptonist/reception_appointment_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Appointment List'
        context["appointments"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context

class ReceponistAppointmentDetailsView(LoginRequiredMixin, ReceptonistPassesTestMixin, DetailView):
    model = AppointmentApplication
    context_object_name = 'appointment'
    template_name = 'receptonist/reception_appointment_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Appointment Details"
        return context