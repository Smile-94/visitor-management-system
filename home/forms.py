from django import forms

# models
from home.models import ContactMessage


class ContactMessage(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = '__all__'