
#Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from employee.permission import EmployeePassesTestMixin

#Generic View Classes
from django.views.generic import DetailView
from django.views.generic import UpdateView

# Models
from employee.models import EmployeeInfo
from employee.models import SocialMediaLink

from employee.forms import SocialMediaLinkForm


class EmployeeProfileView(LoginRequiredMixin, EmployeePassesTestMixin, DetailView):

    model = EmployeeInfo
    context_object_name = 'employee'
    template_name = 'employee/employee_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee Profile" 
        return context






    

