
from django import forms

#models
from visitor.models import VisitorInfo
from visitor.models import VisitorMediaLink


class VisitorInfoForm(forms.ModelForm):

    class Meta:
        model=VisitorInfo
        exclude=('user',)

class VisitorMediaLinkForm(forms.ModelForm):
    
    class Meta:
        model = VisitorMediaLink
        exclude = ('link_of',)
