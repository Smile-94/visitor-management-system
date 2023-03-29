from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
from datetime import date

# Generic View Class
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView


# Models
from accounts.models import User
from home.models import ContactMessage
from employee.models import EmployeeInfo
from appointment.models import Appointment

# forms
from home.forms import ContactMessageForm

class HomveView(TemplateView):
    template_name = 'home/home.html'
    form_class = ContactMessageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home" 
        context["form"] = self.form_class
        return context

class EmployeeListView(ListView):
    model = EmployeeInfo
    queryset = EmployeeInfo.objects.filter(is_active=True, info_of__is_receptonist=False)
    context_object_name = 'employees'
    template_name = 'home/appointment.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Appointment" 
        return context

class ApplintmentListView(ListView):
    Model = Appointment
    queryset = Appointment.objects.filter(is_active=True,appointment_date__gte=date.today())
    template_name = 'home/appointment_list.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        user = User.objects.get(id=pk)
        context = super().get_context_data(**kwargs)
        context["title"] = 'Appointment List'
        context["appointments"] = self.queryset.filter(appointment_of=user)
        return context
    
    

class ContactMessageView(CreateView):
    model = ContactMessage
    form_class = ContactMessageForm
    http_method_names = ['get', 'post']

    def form_valid(self, form):

        if form.is_valid():
            form.save()
            messages.success(self.request, "Message send successfully")
            data={
                'ok':'ok'
            }
            return JsonResponse({'message': 'success', 'data': {'error_message': 'There was a problem processing your request.'}})
        else:
            return JsonResponse({'message': 'error', 'data': form.errors})


    