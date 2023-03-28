from django.shortcuts import render



# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from visitor.permission import VisitorPassesTestMixin

# Django class based view
from django.views import View
from django.views.generic import TemplateView

# Models
from appointment.models import AppointmentApplication



# Create your views here.
class VisitorHomeView(LoginRequiredMixin, VisitorPassesTestMixin, TemplateView):
    template_name = 'visitor/index.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Visitor Home"
        context["pending_appointment"] = AppointmentApplication.objects.filter(request_by=self.request.user, accept_status=False, decline_status=False).count() 
        context["accpted_appointment"] = AppointmentApplication.objects.filter(request_by=self.request.user, accept_status=True, decline_status=False, cancel_status=True).count() 
        context["declined_appointment"] = AppointmentApplication.objects.filter(request_by=self.request.user, accept_status=False, decline_status=True, cancel_status=False).count() 
        context["cancel_appointment"] = AppointmentApplication.objects.filter(request_by=self.request.user, accept_status=True, decline_status=False, cancel_status=True).count() 
        return context
    
