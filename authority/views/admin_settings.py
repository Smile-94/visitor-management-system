from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permission import AdminPassesTestMixin

# Filters
from employee.filters import DesignationInfoFilter

# Generics Views
from django.views.generic import CreateView
from django.views.generic import UpdateView

# Models 
from employee.models import DesignationInfo

# Forms 
from employee.forms import DesignationInfoForm

class DesignationSettingsView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = DesignationInfo
    queryset= DesignationInfo.objects.filter(is_active=True)
    form_class = DesignationInfoForm
    filterset_class = DesignationInfoFilter
    template_name = 'authority/add_designation.html'
    success_url = reverse_lazy('authority:designation_info')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add Designation'
        context["designations"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Designation Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong please try again")
        return super().form_invalid(form)
    

class DesignationUpdateView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = DesignationInfo
    fields = ('designation', 'department', 'description')
    template_name = 'authority/add_designation.html'
    success_url = reverse_lazy('authority:designation_info')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Designation" 
        context["updated"] = True 
        return context

    def form_valid(self, form):
        messages.success(self.request, "Designation Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "some thing went wrong try again")
        return super().form_invalid(form)
