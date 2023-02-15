from django import forms

# models
from employee.models import EmployeeInfo
from employee.models import DesignationInfo

# Widgets
from employee.widgets import CustomPictureImageFieldWidget
from employee.widgets import CustomSignetureImageFieldWidget


class EmployeeInfoForm(forms.ModelForm):
    employee_id = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    signature = forms.ImageField(widget=CustomSignetureImageFieldWidget)

    class Meta:
        model = EmployeeInfo
        exclude = ('info_of', 'is_active')


class DesignationInfoForm(forms.ModelForm):
    
    class Meta:
        model = DesignationInfo
        exclude = ('is_active',)