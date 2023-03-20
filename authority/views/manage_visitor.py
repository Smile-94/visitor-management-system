from django.urls import reverse_lazy
from django.shortcuts import redirect
# Generic Classes
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView

# Permission Calsses
from django.contrib.auth.mixins import LoginRequiredMixin
from authority.permission import AdminPassesTestMixin

# Models
from accounts.models import User

# Filter Classes
from accounts.filters import UserFilter

class VisitorListView(LoginRequiredMixin, AdminPassesTestMixin, ListView ):
    model = User
    queryset = User.objects.filter(is_visitor=True, is_active=True).order_by('-id')
    filterset_class = UserFilter
    template_name = 'authority/visitor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Visitors" 
        context["visitors"] = self.filterset_class(self.request.GET, queryset=self.queryset)
        return context

class VisitorDetailView(LoginRequiredMixin, AdminPassesTestMixin, DetailView):
    model = User
    context_object_name='visitor'
    template_name = 'authority/visitor_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Visitor Details" 
        return context

class DeleteVisitorView(LoginRequiredMixin, AdminPassesTestMixin, DeleteView):
    model= User
    context_object_name='visitor'
    template_name = "authority/delete_visitor.html"
    success_url = reverse_lazy('authority:visitor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Visitor" 
        return context

    def form_valid(self, form):
        self.object.is_active = False
        self.object.save()
        return redirect(self.success_url)
    