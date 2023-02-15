from django.shortcuts import render
from django.shortcuts import HttpResponse

# class based views
from django.views import View
# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(View):

    def get(self,request,*args, **kwargs):
        contex_data={
            'title':'Home',
        }
        return HttpResponse("Home page will implemented soon")