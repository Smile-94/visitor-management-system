from django import forms

# models
from home.models import ContactMessage


class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = '__all__'