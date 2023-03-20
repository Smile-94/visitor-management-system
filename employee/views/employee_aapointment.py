from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

# permission class
from django.contrib.auth.mixins import LoginRequiredMixin
from employee.permission import EmployeePassesTestMixin

# Generic classes
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Models
from appointment.models import Appointment

# Forms
from appointment.forms import AppointmentForm

# Filters
from appointment.filters import AppointmentFilter


# View Start from here
class AppointmentView(LoginRequiredMixin, EmployeePassesTestMixin, CreateView):
    model = Appointment
    queryset =Appointment.objects.filter(is_active=True).order_by('-id')
    form_class = AppointmentForm
    filterset_class = AppointmentFilter
    template_name = "employee/add_appointment.html"
    success_url = reverse_lazy('employee:add_appointment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Appointment"
        context["appointments"] = self.filterset_class(self.request.GET, queryset=self.queryset) 
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            user_info=form.save(commit=False)
            user_info.appointment_of=self.request.user
            user_info.save()
            messages.success(self.request, "Appointment Added Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong try again!")
        return super().form_invalid(form)

class AppointmentUpdateView(LoginRequiredMixin, EmployeePassesTestMixin, UpdateView):
    model=Appointment
    form_class=AppointmentForm
    template_name='employee/add_appointment.html'
    success_url= reverse_lazy('employee:add_appointment')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Appointment"
        context["updated"] = True
        return context
    
    def form_valid(self, form):
        messages.success(self.request, "Appointment Updated Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Something wrong appointment not updated")
        return super().form_invalid(form)

class DeleteAppointmentView(LoginRequiredMixin, EmployeePassesTestMixin, DeleteView):
    model= Appointment
    context_object_name='appointment'
    template_name = "employee/add_appointment.html"
    success_url = reverse_lazy('employee:add_appointment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Appointment" 
        context["deleted"] = True 
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)

    
    