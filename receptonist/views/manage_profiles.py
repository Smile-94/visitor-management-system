from django.urls import reverse_lazy
from django.contrib import messages

#Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from receptonist.permissions import ReceptonistPassesTestMixin

#Generic View Classes
from django.views.generic import DetailView
from django.views.generic import UpdateView

# Models
from employee.models import EmployeeInfo
from employee.models import SocialMediaLink

from employee.forms import SocialMediaLinkForm


class ReceptonistProfileView(LoginRequiredMixin, ReceptonistPassesTestMixin, DetailView):

    model = EmployeeInfo
    context_object_name = 'employee'
    template_name = 'receptonist/receptonist_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Receptonist Profile" 
        return context
    
class ReceptonistSocialMediaLinkView(LoginRequiredMixin, ReceptonistPassesTestMixin, UpdateView):

    model = SocialMediaLink
    form_class = SocialMediaLinkForm
    template_name = 'employee/social_media_link.html'
    success_url = reverse_lazy('employee:employee_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee Social Media Link" 
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Updated Successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Some thing worng try again!")
        return super().form_invalid(form)