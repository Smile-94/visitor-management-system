
from django import forms

#models
from visitor.models import VisitorInfo


class VisitorInfoForm(forms.ModelForm):

    class Meta:
        model=VisitorInfo
        exclude=('user',)
