from django.urls import path

# Views
from authority.views import authority_main
from authority.views import add_employee
from authority.views import admin_settings


app_name = 'authority'

urlpatterns = [
    path('authority-home/', authority_main.AdminHomeView.as_view(), name="authority_home"),
    
]

# add update view employee

urlpatterns += [
    path('add-employee/', add_employee.AddEmployeeView.as_view(), name="add_employee"),
    path('add-employee-info/<int:pk>/', add_employee.AddEmployeeInfoView.as_view(), name="add_employee_info"),
    path('add-employee-address/<int:pk>/', add_employee.AddEmployeeAddressView.as_view(), name="add_employee_address"),
    path('employee-detail/<int:pk>/', add_employee.EmployeeDetailView.as_view(), name="employee_detail"),
    path('delete-employee/<int:pk>/', add_employee.DeleteEmployeeView.as_view(), name="delete_employee"),
]

# Admin Settings url path
urlpatterns += [
    path('desingation-info/', admin_settings.DesignationSettingsView.as_view(), name='designation_info'),
    path('update-desingation/<int:pk>/', admin_settings.DesignationUpdateView.as_view(), name='update_designation')
]


