import django_filters
from django import forms

# Models
from appointment.models import Appointment
from appointment.models import AppointmentApplication
from appointment.models import OnArivalAppointmentApplication

class AppointmentFilter(django_filters.FilterSet):
    appointment_date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))
    meet_from = django_filters.TimeFilter(widget=forms.TimeInput(attrs={'type': 'time'}))
    meet_to = django_filters.TimeFilter(widget=forms.TimeInput(attrs={'type': 'time'}))


    class Meta:
        model = Appointment
        fields = ('appointment_date','meet_from','meet_to',)


class PendingAppointmentApplicationFilter(django_filters.FilterSet):
    from_date = django_filters.DateFilter(field_name='request_date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='From')
    to_date = django_filters.DateFilter(field_name='request_date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}), label='To')

    class Meta:
        model = AppointmentApplication
        fields = ('appointment_id', 'request_date')

class OnArivalAppointmentFilter(django_filters.FilterSet):
    from_date = django_filters.DateFilter(field_name='appointment_date', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='From')
    to_date = django_filters.DateFilter(field_name='appointment_date', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}), label='To')

    class Meta:
        model = OnArivalAppointmentApplication
        fields = ('appointment_id','appointment_date')
        
