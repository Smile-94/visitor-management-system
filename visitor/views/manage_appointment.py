from django.urls import reverse_lazy
from django.contrib import messages
from datetime import datetime

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from visitor.permission import VisitorPassesTestMixin

# Generic Classes
from django.views.generic import ListView

# Models 
from appointment.models import Appointment
from employee.models import EmployeeInfo

class EmployeeListView(ListView):
    model = EmployeeInfo
    template_name = 'visito/employee_list'







