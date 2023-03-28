from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

# class based view
from django.views import View
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# login and logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import SignUpForm

# models
from accounts.models import User


# Create your views here.

# Signup View for Visitor to create visitor accounts
class SignupVisitor(View):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('visitor:visitor_home')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        contex_data = {
            'title': 'Signup',
            'form': form
        }
        return render(request, self.template_name, context=contex_data)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_visitor = True
            user.save()
            messages.success(request, 'Your account create successfully please fill up other information')
            return redirect(self.success_url)
            
        else:
            try:
                if User.objects.filter(email=request.POST['email']).exists():
                    messages.error(request, f"{request.POST['email']} is exitst")
            except Exception as e:
                print(e)

            contex_data = {
                'title': 'Signup Visitor',
                'form': form
            }
        return render(request, self.template_name, context=contex_data)


# Signup view class for employee to create employee accounts
class SignupEmployee(View):
    form_class = SignUpForm
    success_url = reverse_lazy('authority:add_employee')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_employee = True
            user.save()
            messages.success(request, 'Your account create successfully please fill up other information')
            return redirect(self.success_url)
            
        else:
            try:
                if User.objects.filter(email=request.POST['email']).exists():
                    messages.error(request, f"{request.POST['email']} is exitst")
            except Exception as e:
                print(e)

            contex_data = {
                'title': 'Signup',
                'form': form
            }
        return render(request, self.template_name, context=contex_data)


class UserLoginView(View):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home:index')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context_data = {
            'title': 'Login',
            'form': form
        }
        return render(request, self.template_name, context=context_data)
    
    def post(self, request, *args, **kwargs):
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            request_user = User.objects.get(email=username)

            if user is not None and request_user.is_visitor is True:
                login(request, user)
               
                if 'next' in request.POST:
                    redirect_url = request.POST.get('next')
                    return redirect(redirect_url)
                else:
                    return HttpResponseRedirect(reverse('visitor:visitor_home'))
                
            elif user is not None and request_user.is_employee is True and request_user.is_receptonist is True:
                login(request, user)
                messages.success(request, 'Welcome to your user panel')
                return HttpResponseRedirect(reverse('receptonist:receptonist'))


            elif user is not None and request_user.is_employee is True:
                login(request, user)
                messages.success(request, 'Welcome to your user panel')
                return HttpResponseRedirect(reverse('employee:employee_home'))
                
            elif user is not None and not request_user.is_visitor and not request_user.is_employee:
                login(request, user)
                messages.success(request, 'Welcome to your user panel')
                return HttpResponseRedirect(reverse('authority:authority_home', ))
                
            else:
                messages.error(request, 'User name or password invalid, try again!')
                return redirect(reverse('accounts:login'))
        
        except Exception as e:
            print(e)
            messages.error(request, 'User name or password invalid, try again!')
            return redirect(reverse('accounts:login'))
    

class UserLogoutView(LoginRequiredMixin,LogoutView):
    
    template_name = 'accounts/login.html'
    extra_context = {'form': AuthenticationForm}

    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect(reverse('accounts:login'))
