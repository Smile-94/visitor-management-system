from django import forms
import django_filters

# Models
from employee.models import DesignationInfo
from employee.models import EmployeeInfo


class DesignationInfoFilter(django_filters.FilterSet):

    designation = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = DesignationInfo
        fields = ('designation','department')


DEPARTMENT_OPT = (
    ('HR', 'Human Resource'),
    ('administrative', 'Administrative'),
    ('software development', 'Software Development'),
    ('QA', 'Quality Assurance'),
    ('project management', 'Project Management'),
    ('Product Management', 'Product Management'),
    ('design', 'Design'),
    ('devOps', 'DevOps'),
    ('customer support', 'Customer Support'),
    ('marketing', 'Marketing'),
    ('IT', 'Information Technology')
)

class EmployeeInfoFilter(django_filters.FilterSet):
    employee_id = django_filters.CharFilter(lookup_expr='icontains')
    position__designation = django_filters.CharFilter(lookup_expr='icontains')
    position__department = django_filters.ChoiceFilter(choices=DEPARTMENT_OPT)

    class Meta:
        model = EmployeeInfo
        fields = ['employee_id', 'position__designation', 'position__department']
