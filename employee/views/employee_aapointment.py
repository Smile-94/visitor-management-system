from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
# from datetime import datetime
import datetime

# permission class
from django.contrib.auth.mixins import LoginRequiredMixin
from employee.permission import EmployeePassesTestMixin

# Generic classes
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import DetailView

# Models
from accounts.models import User
from appointment.models import Appointment
from appointment.models import AppointmentApplication

# Forms
from appointment.forms import AppointmentForm
from appointment.forms import AppointmentAcceptForm
from appointment.forms import AppointmentDeclineForm
from appointment.forms import AppointmentCancelForm

# Filters
from appointment.filters import AppointmentFilter
from appointment.filters import PendingAppointmentApplicationFilter


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

class EmployeePendingAppointmentView(LoginRequiredMixin, EmployeePassesTestMixin, ListView):
    Model = AppointmentApplication
    queryset = AppointmentApplication.objects.filter(is_active=True, accept_status=False, decline_status=False)
    filterset_class = PendingAppointmentApplicationFilter
    template_name = 'employee/pending_appointment_list.html'

    def get_queryset(self):
        self.queryset = self.queryset.filter(appointment_of__appointment_of=self.request.user).order_by('-id')
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Appointment List'
        context["appointments"] = self.filterset_class(self.request.GET, queryset=self.get_queryset())
        return context

class EmployeeAcceptedApointmentListView(LoginRequiredMixin, EmployeePassesTestMixin, ListView):
    Model = AppointmentApplication
    queryset = AppointmentApplication.objects.filter(is_active=True, accept_status=True, decline_status=False, cancel_status=False)
    filterset_class = PendingAppointmentApplicationFilter
    template_name = 'employee/accepted_appointment_list.html'

    def get_queryset(self):
        self.queryset = self.queryset.filter(appointment_of__appointment_of=self.request.user).order_by('-id')
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Appointment List'
        context["appointments"] = self.filterset_class(self.request.GET, queryset=self.get_queryset())
        return context

class DeclinedAppointmentListView(LoginRequiredMixin, EmployeePassesTestMixin, ListView):
    Model = AppointmentApplication
    queryset = AppointmentApplication.objects.filter(is_active=True, accept_status=False, decline_status=True)
    filterset_class = PendingAppointmentApplicationFilter
    template_name = 'employee/declined_appointment_list.html'

    def get_queryset(self):
        self.queryset = self.queryset.filter(appointment_of__appointment_of=self.request.user).order_by('-id')
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Declined Appointment List'
        context["appointments"] = self.filterset_class(self.request.GET, queryset=self.get_queryset())
        return context

class CancelAppointmentListView(LoginRequiredMixin, EmployeePassesTestMixin, ListView):
    Model = AppointmentApplication
    queryset = AppointmentApplication.objects.filter(is_active=True, cancel_status=True)
    filterset_class = PendingAppointmentApplicationFilter
    template_name = 'employee/cancel_appointment_list.html'

    def get_queryset(self):
        self.queryset = self.queryset.filter(appointment_of__appointment_of=self.request.user).order_by('-id')
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cancel Appointment List'
        context["appointments"] = self.filterset_class(self.request.GET, queryset=self.get_queryset())
        return context

class AcceptAppointmentView(LoginRequiredMixin, EmployeePassesTestMixin, UpdateView):
    model = AppointmentApplication
    form_class = AppointmentAcceptForm
    template_name = 'employee/appointment_accept.html'
    success_url = reverse_lazy('employee:employee_appointment_details', kwargs={'pk': 0})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accept Appointment" 
        return context
    
    def form_valid(self, form):
        try:

            if form.is_valid():
                form_obj= form.save(commit=False)
                form_obj.accept_status = True
                form_obj.approved_date = datetime.date.today()
                form_obj.save() 

            # Send Mail
                try:
                    subject = 'Accept Appointment'
                    message = self.object.message
                    from_email = 'vsmpsm2023@gmail.com'
                    recipient_list = [ self.object.request_by.email,]
                    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                except Exception as e:
                    print(e)

                messages.success(self.request, "Appointment Accept Successfully")
                self.success_url = reverse_lazy('employee:employee_appointment_details', kwargs={'pk': self.object.id})
        except Exception as e:
            print(e)
            self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Something wrong try again!')
        return super().form_invalid(form)

class DeclineAppointmentView(LoginRequiredMixin, EmployeePassesTestMixin, UpdateView):
    model = AppointmentApplication
    form_class = AppointmentDeclineForm
    template_name = 'employee/appointment_accept.html'
    success_url = reverse_lazy('employee:employee_appointment_details', kwargs={'pk': 0})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accept Appointment" 
        return context
    
    def form_valid(self, form):
        try:

            if form.is_valid():
                form_obj= form.save(commit=False)
                form_obj.decline_status = True
                form_obj.approved_date = datetime.date.today()
                form_obj.save() 

            # Send Mail
                try:
                    subject = 'Decline Appointment'
                    message = self.object.message
                    from_email = 'vsmpsm2023@gmail.com'
                    recipient_list = [ 'mshossen75@gmail.com',]
                    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                except Exception as e:
                    print(e)

                    messages.warning(self.request, "Appointment Declined Successfully")
                    self.success_url = reverse_lazy('employee:employee_appointment_details', kwargs={'pk': self.object.id})

        except Exception as e:
            print(e)
            self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Something wrong try again!')
        return super().form_invalid(form)

class CancelAppointmentView(LoginRequiredMixin, EmployeePassesTestMixin, UpdateView):
    model = AppointmentApplication
    form_class = AppointmentCancelForm
    template_name = 'employee/appointment_accept.html'
    success_url = reverse_lazy('employee:employee_appointment_details', kwargs={'pk': 0})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Accept Appointment" 
        return context
    
    def form_valid(self, form):
        try:

            if form.is_valid():
                form_obj= form.save(commit=False)
                form_obj.cancel_status = True
                form_obj.save() 

                # Send Mail
                try:
                    subject = 'Cancel Appointment'
                    message = self.object.cancel_message
                    from_email = 'vsmpsm2023@gmail.com'
                    recipient_list = [ 'mshossen75@gmail.com',]
                    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                except Exception as e:
                    print(e)
                messages.warning(self.request, "Appointment Cancel Successfully")
                print("Self Object: ",self.object.id)
                self.success_url = reverse_lazy('employee:employee_appointment_details', kwargs={'pk': self.object.id})

        except Exception as e:
            print(e)
            self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Something wrong try again!')
        return super().form_invalid(form)


class EmployeeAppointmentDetailsView(LoginRequiredMixin, EmployeePassesTestMixin, DetailView):
    model = AppointmentApplication
    context_object_name = 'appointment'
    template_name = 'employee/appointment_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Appointment Details"
        context["accept_form"] = AppointmentAcceptForm
        context["decline_form"] = AppointmentDeclineForm
        context["cancel_form"] = AppointmentCancelForm
        return context

class AppointmentVisitorProfileView(LoginRequiredMixin, EmployeePassesTestMixin, DetailView):
    model = User
    context_object_name = 'visitor'
    template_name = 'employee/visitor_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Visitor Profile' 
        return context
    
    
    