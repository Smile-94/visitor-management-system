from django.urls import reverse_lazy
from django.contrib import messages

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from receptonist.permissions import ReceptonistPassesTestMixin

# Generic Classes
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView

# Models
from appointment.models import AppointmentApplication

# Forms
from appointment.forms import IssuedAppointmentForm

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
        context["form"] = IssuedAppointmentForm
        return context


class IssuedAppointmentView(LoginRequiredMixin, ReceptonistPassesTestMixin, UpdateView):
    model = AppointmentApplication
    form_class = IssuedAppointmentForm
    template_name = 'receptonist/issued_appointment.html'
    success_url = reverse_lazy('receptonist:receptonist_appoinment_details', kwargs={'pk': 0})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Issued Appointment"
        return context
    
    def form_valid(self, form):
        
        try:
            if form.is_valid():
                form_obj= form.save(commit=False)
                form_obj.issued_status = True
                form_obj.issued_by = self.request.user
                form_obj.save()
                messages.success(self.request, "Appointment Issued Successfully! ")
                self.success_url= reverse_lazy('receptonist:receptonist_appoinment_details', kwargs={'pk': self.object.id})
        except Exception as e:
            print(e)
            return self.form_invalid(form)
        return super().form_valid(form)
    