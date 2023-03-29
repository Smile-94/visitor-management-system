from django import forms

# models
from appointment.models import Appointment
from appointment.models import AppointmentApplication


class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    meet_from = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    meet_to = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model=Appointment
        fields = ('appointment_date','meet_from','meet_to',)


class AppointmentApplicationForm(forms.ModelForm):

    class Meta:
        model = AppointmentApplication
        fields = ('heading','description')


class AppointmentAcceptForm(forms.ModelForm):
    meeting_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = AppointmentApplication
        fields = ('meeting_time','message')

class AppointmentDeclineForm(forms.ModelForm):

    class Meta:
        model = AppointmentApplication
        fields = ('message',)

class AppointmentCancelForm(forms.ModelForm):

    class Meta:
        model = AppointmentApplication
        fields = ('cancel_message',)

class IssuedAppointmentForm(forms.ModelForm):
    entering_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = AppointmentApplication
        fields = ('entering_time',)


class IssuedAppointmentExitForm(forms.ModelForm):
    exit_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    
    class Meta:
        model = AppointmentApplication
        fields = ('exit_time',)
