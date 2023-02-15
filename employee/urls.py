from django.urls import path

# Views
from employee.views import EmployeeHomeView


app_name='employee'

urlpatterns = [

    path('employee-home/', EmployeeHomeView.as_view(), name='employee_home')
    
]
