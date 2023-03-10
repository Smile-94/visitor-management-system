from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages

# Generic View Class
from django.views.generic import TemplateView
from django.views.generic import CreateView


# Models
from home.models import ContactMessage

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


    