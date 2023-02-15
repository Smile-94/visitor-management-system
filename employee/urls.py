from django.urls import path

# Views
from employee.views import employee_main


app_name='employee'

urlpatterns = [

    path('employee-home/', employee_main.EmployeeHomeView.as_view(), name='employee_home')
    
]
