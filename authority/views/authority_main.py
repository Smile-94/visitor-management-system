
# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from authority.permission import AdminPassesTestMixin

# class Based View
from django.views.generic import TemplateView

# Models
from employee.models import EmployeeInfo
from visitor.models import VisitorInfo
from appointment.models import AppointmentApplication



# Create your views here.
class AdminHomeView(LoginRequiredMixin, AdminPassesTestMixin, TemplateView):

    template_name='authority/authority.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Admin Panel"
        context["total_employee"] = EmployeeInfo.objects.all().count()
        context["total_visitor"] = VisitorInfo.objects.all().count()
        context["total_appointment"] = VisitorInfo.objects.all().count()
        context["total_appointment"] = AppointmentApplication.objects.all().count()
        return context

