
from django.urls import reverse_lazy
from django.contrib import messages

# Generic classes
from django.views.generic import CreateView

# Models
from appointment.models import Appointment

from appointment.forms import AppointmentForm

class AppointmentView(CreateView):
    pass