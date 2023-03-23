from django.urls import reverse_lazy
from django.contrib import messages
import datetime
from django.urls import reverse

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from visitor.permission import VisitorPassesTestMixin

# Generic Classes
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView

# Models 
from appointment.models import Appointment
from appointment.models import AppointmentApplication
from employee.models import EmployeeInfo
from appointment.forms import AppointmentApplicationForm


class EmployeeListView(ListView):
    model = EmployeeInfo
    template_name = 'visito/employee_list'

class TakeAppointmentView(LoginRequiredMixin, VisitorPassesTestMixin, CreateView):
    model = AppointmentApplication
    form_class = AppointmentApplicationForm
    template_name = 'visitor/appointment_application.html'
    success_url = reverse_lazy('visitor:visitor_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Take Appointment" 
        return context
    
    def form_valid(self, form):
        try:
            appoint_pk= self.kwargs.get('pk')
            appointment_obj= Appointment.objects.get(id=appoint_pk)
            if form.is_valid():
                form_obj= form.save(commit=False)
                form_obj.request_by = self.request.user
                form_obj.appointment_of = appointment_obj
                form_obj.save() 
        
        except Exception as e:
            print(e)
            self.form_invalid(form)

        return super().form_valid(form)

class PendingAppointmentListView(LoginRequiredMixin, VisitorPassesTestMixin, ListView):
    Model = AppointmentApplication
    queryset = AppointmentApplication.objects.filter(is_active=True, accept_status=False, decline_status=False)
    context_object_name = 'appointments'
    template_name = 'visitor/pending_appointment_list.html'

    def get_queryset(self):
        self.queryset = self.queryset.filter(request_by=self.request.user)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Appointment List'
        return context


class AppointmentDetailsView(LoginRequiredMixin, VisitorPassesTestMixin, DetailView):
    model = AppointmentApplication
    context_object_name = 'appointment'
    template_name = 'visitor/appointment_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Appointment Details"
        return context
    
    
    







