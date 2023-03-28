from django.shortcuts import render

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from employee.permission import EmployeePassesTestMixin

# Models
from appointment.models import AppointmentApplication

# Create your views here.
from django.views.generic import TemplateView

class EmployeeHomeView(LoginRequiredMixin, EmployeePassesTestMixin, TemplateView):
    template_name='employee/employee.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee Panel"
        context["pending_appointment"] = AppointmentApplication.objects.filter(appointment_of__appointment_of=self.request.user, accept_status=False, decline_status=False).count()
        context["canceled_appointment"] = AppointmentApplication.objects.filter(appointment_of__appointment_of=self.request.user, accept_status=True, decline_status=False, cancel_status=True).count()
        context["accpted_appointment"] = AppointmentApplication.objects.filter(appointment_of__appointment_of=self.request.user, accept_status=True, decline_status=False, cancel_status=False).count()
        context["declined_appointment"] = AppointmentApplication.objects.filter(appointment_of__appointment_of=self.request.user, accept_status=False, decline_status=True, cancel_status=False).count()
        return context
