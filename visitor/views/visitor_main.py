from django.shortcuts import render



# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

# Django class based view
from django.views import View



# Create your views here.
class VisitorHomeView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'visitor/index.html'

    # User pass test to view the visitor home view
    def test_func(self):
        return self.request.user.is_visitor

    def get(self, request, *args, **kwargs):

        context_data = {
            'title': 'Visitor Home'
        }
        return render(request, self.template_name, context=context_data)
