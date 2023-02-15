from django import forms

# models
from appointment.models import Appointment


class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    meet_from = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    meet_to = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model=Appointment
        fields = ('appointment_date','meet_from','meet_to',)


class AppointmentCancelForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('cancel_message',)