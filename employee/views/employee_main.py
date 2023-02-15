from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class EmployeeHomeView(TemplateView):
    template_name='employee/employee.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee Panel"
        return context
