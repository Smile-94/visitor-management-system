from django import forms

# models
from appointment.models import Appointment


class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    meet_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'time'}))
    meet_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'time'}))

    class Meta:
        model=Appointment
        exclude = ('appointment_of','is_active','cancel_status','cancel_message')