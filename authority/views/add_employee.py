from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


# Permissions and Authorization
from django.contrib.auth.mixins import LoginRequiredMixin

# custom UserpassTestMixin
from authority.permission import AdminPassesTestMixin

# class Based View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Models
from accounts.models import User
from accounts.models import PresentAddress
from employee.models import EmployeeInfo

# forms
from accounts.forms import SignUpForm
from accounts.forms import ProfileForm
from accounts.forms import PresentAddressForm
from accounts.forms import PermanentAddressForm
from employee.forms import EmployeeInfoForm

# Filters
from accounts.filters import UserFilter


class AddEmployeeView(LoginRequiredMixin, AdminPassesTestMixin, CreateView):
    model = User
    queryset = User.objects.filter(is_employee=True, is_active=True).order_by('-id')
    form_class= SignUpForm
    filterset_class = UserFilter
    template_name='authority/add_employee.html'
    success_url= reverse_lazy('authority:authority_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employees" 
        context["users"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context
    
    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.is_employee = True
            user.save()
            messages.success(self.request, "Employee Accounts Created Success Fully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "email or password invalid try aging")
        return super().form_invalid(form)

class EmployeeDetailView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = User
    context_object_name='employee'
    template_name = 'authority/employee_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee Details" 
        return context
    

class AddEmployeeInfoView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = User
    model2 = EmployeeInfo
    form_class = ProfileForm
    form_class2 = EmployeeInfoForm
    template_name = 'authority/add_employee_info.html'
    success_url = reverse_lazy('authority:add_employee')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_object = User.objects.get(id=self.kwargs.get('pk'))
            print(user_object)
            context["title"] = "Add/Edit Employee Inof"
            context["form"] = self.form_class(instance=user_object.profile)
            context["form2"] = self.form_class2(instance=user_object.employee_info)
            
        except Exception as e:
            print(e)
        return context
    
    def post(self, request, *args, **kwargs):
        user_object = User.objects.get(id=self.kwargs.get('pk'))
        form = self.form_class(request.POST, request.FILES, instance=user_object.profile)
        form2 = self.form_class2(request.POST, request.FILES, instance=user_object.employee_info)
        return self.form_valid(form, form2)
    
    def form_valid(self, form, form2):
        try:
            if form.is_valid() and form2.is_valid():
                user = form.save(commit=False)
                info = form2.save(commit=False)
                user.profile = User.objects.get(id=self.kwargs.get('pk'))
                info.info_of = User.objects.get(id=self.kwargs.get('pk'))
                user.save()
                info.save()
                messages.success(self.request, "Employee Info Updated Successfully")
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return super().form_invalid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Some thing wrong try again")
        return super().form_invalid(form)


class AddEmployeeAddressView(LoginRequiredMixin, AdminPassesTestMixin, UpdateView):
    model = User
    model2 = PresentAddress
    form_class = PresentAddressForm
    form_class2 = PermanentAddressForm
    template_name = 'authority/add_employee_address.html'
    success_url = reverse_lazy('authority:add_employee')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_object = User.objects.get(id=self.kwargs.get('pk'))
            print(user_object)
            context["title"] = "Add/Edit Employee Inof"
            context["form"] = self.form_class(instance=user_object.present_address)
            context["form2"] = self.form_class2(instance=user_object.permanent_address)
            
        except Exception as e:
            print(e)
        return context
    
    def post(self, request, *args, **kwargs):
        user_object = User.objects.get(id=self.kwargs.get('pk'))
        form = self.form_class(request.POST, request.FILES, instance=user_object.present_address)
        form2 = self.form_class2(request.POST, request.FILES, instance=user_object.permanent_address)
        return self.form_valid(form, form2)
    
    def form_valid(self, form, form2):
        try:
            if form.is_valid() and form2.is_valid():
                present_address = form.save(commit=False)
                parmanent_address = form2.save(commit=False)
                present_address.address_of = User.objects.get(id=self.kwargs.get('pk'))
                parmanent_address.address_of = User.objects.get(id=self.kwargs.get('pk'))
                present_address.save()
                parmanent_address.save()
                messages.success(self.request, "Employee Info Updated Successfully")
            return super().form_valid(form)

        except Exception as e:
            print(e)
            return super().form_invalid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Some thing wrong try again")
        return super().form_invalid(form)

class DeleteEmployeeView( LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= User
    context_object_name='employee'
    template_name = "authority/delete_employee.html"
    success_url = reverse_lazy('authority:add_employee')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Visitor" 
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)
    
    
    
    
