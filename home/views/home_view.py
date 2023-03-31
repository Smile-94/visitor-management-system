from django.db.models import Avg
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages
from datetime import date

# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin

# Generic View Class
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView


# Models
from accounts.models import User
from home.models import ContactMessage
from employee.models import EmployeeInfo
from employee.models import Review
from appointment.models import Appointment

# forms
from home.forms import ContactMessageForm
from employee.forms import ReviewForm

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

class EmployeeDetailsView(DetailView):
    model = EmployeeInfo
    context_object_name = 'employee'
    template_name = 'home/employee_review.html'

    def get_context_data(self, **kwargs):
        employee_pk = self.kwargs['pk']
        employee_obj= EmployeeInfo.objects.get(id=employee_pk)
        reviews = Review.objects.filter(review_of=employee_obj.info_of)
        context = super().get_context_data(**kwargs)
        context["title"] = "employee Details"
        context["form"] = ReviewForm
        context["reviews"] = Review.objects.filter(review_of=employee_obj.info_of).order_by('-created_at')[:10]
        context["total_rating"] = reviews.aggregate(avg_rating=Avg('rating'))
        return context

class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'home/create_review.html'
    success_url = reverse_lazy('home:employee_details', kwargs={'pk': 0})
    
    def get_context_data(self, **kwargs):
        employee_pk = self.kwargs['pk']
        employee_obj= EmployeeInfo.objects.get(id=employee_pk)
        reviews = Review.objects.filter(review_of=employee_obj.info_of)
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Review"
        context["employee"] = EmployeeInfo.objects.get(id=self.kwargs['pk'])
        context["reviews"] = Review.objects.filter(review_of=employee_obj.info_of).order_by('-created_at')[:10]
        context["total_rating"] = reviews.aggregate(avg_rating=Avg('rating'))
        return context
    
    def form_valid(self, form):
        try:
            employee_pk = self.kwargs['pk']
            employee = EmployeeInfo.objects.get(id=employee_pk)

            if form.is_valid():
                form_obj = form.save(commit=False)
                form_obj.review_of= employee.info_of
                form_obj.review_by = self.request.user
                form_obj.save()
                messages.success(self.request, "Thank for revewing, stay with us! ")
                self.success_url = reverse_lazy('home:employee_details', kwargs={'pk': employee_pk})
        except Exception as e:
            print(e)
            return self.form_invalid(form)
        
        return super().form_valid(form)
    

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


    