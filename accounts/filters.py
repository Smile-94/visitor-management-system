import django_filters
from django import forms

# Models
from accounts.models import User


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = User
        fields= ('email',)