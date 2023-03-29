from django.urls import reverse_lazy
from django.contrib import messages

# Generic Classes
from django.views.generic import CreateView
from django.views.generic import ListView

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from receptonist.permissions import ReceptonistPassesTestMixin

# Models
from employee.models import EmployeeInfo
from appointment.models import OnArivalAppointmentApplication

# Filter Classes
from employee.filters import EmployeeInfoFilter
from appointment.filters import OnArivalAppointmentFilter

# Forms Classes
from appointment.forms import OnArivalAppointApplicationForm




class OnArivalAppointmentView(LoginRequiredMixin, ReceptonistPassesTestMixin, CreateView):
    model = OnArivalAppointmentApplication
    queryset = EmployeeInfo.objects.filter(is_active=True, info_of__is_receptonist=False)
    form_class= OnArivalAppointApplicationForm
    filterset_class = EmployeeInfoFilter
    template_name='receptonist/employee_list.html'
    success_url= reverse_lazy('receptonist:onarival_employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employees" 
        context["users"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context
    
    def get_initial(self):
        initial = super().get_initial()
        initial['pk'] = self.request.POST.get('pk')
        return initial
    
    def form_valid(self, form):
        try:
            pk = self.get_initial()['pk']
            employee_obj = EmployeeInfo.objects.get(id=pk)
            if form.is_valid():
                form_obj= form.save(commit=False)
                form_obj.appointment_to = employee_obj.info_of
                form_obj.issued_by = self.request.user
                form_obj.issued_status=True
                form_obj.save()
                messages.success(self.request, "On Arival Appointment Added Successfully")
        
        except Exception as e:
            print(e)
        
        return super().form_valid(form)

    
    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong try again!")
        return super().form_invalid(form)

class OnArivalAppointmentListView(LoginRequiredMixin, ReceptonistPassesTestMixin, ListView):
    Model = OnArivalAppointmentApplication
    queryset = OnArivalAppointmentApplication.objects.filter(is_active=True, issued_status=True).order_by('-id')
    filterset_class = OnArivalAppointmentFilter
    template_name = 'receptonist/on_arival_appointment_list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Appointment List'
        context["appointments"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context