import django_filters
from django import forms

# Models
from appointment.models import Appointment

class AppointmentFilter(django_filters.FilterSet):
    appointment_date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))
    meet_from = django_filters.TimeFilter(widget=forms.TimeInput(attrs={'type': 'time'}))
    meet_to = django_filters.TimeFilter(widget=forms.TimeInput(attrs={'type': 'time'}))


    class Meta:
        model = Appointment
        fields = ('appointment_date','meet_from','meet_to',)