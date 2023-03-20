from django.urls import path

# Views
from employee.views import employee_main
from employee.views import employee_aapointment
from employee.views import manage_profile


app_name='employee'

urlpatterns = [
    path('employee-home/', employee_main.EmployeeHomeView.as_view(), name='employee_home') 
]

# Manage Profile 
urlpatterns += [
    path('employee-profile-details/<int:pk>/', manage_profile.EmployeeProfileView.as_view(), name='employee_profile_details')
    
]


# add, update, delete appointment
urlpatterns += [
    path('add_appointment/', employee_aapointment.AppointmentView.as_view(), name= "add_appointment"),
    path('update-appointment/<int:pk>/', employee_aapointment.AppointmentUpdateView.as_view(), name= "update_appointment"),
    path('delete-appointment/<int:pk>/', employee_aapointment.DeleteAppointmentView.as_view(), name= "delete_appointment"),
    
]
