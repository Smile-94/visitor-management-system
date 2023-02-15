from django.urls import path

# Views
from employee.views import employee_main
from employee.views import employee_aapointment


app_name='employee'

urlpatterns = [
    path('employee-home/', employee_main.EmployeeHomeView.as_view(), name='employee_home') 
]

# add, update, delete appointment
urlpatterns += [
    path('add_appointment/', employee_aapointment.AppointmentView.as_view(), name= "add_appointment"),
    path('update-appointment/<int:pk>/', employee_aapointment.AppointmentUpdateView.as_view(), name= "update_appointment"),
    path('delete-appointment/<int:pk>/', employee_aapointment.DeleteAppointmentView.as_view(), name= "delete_appointment"),
    path('cancel-appointment/<int:pk>/', employee_aapointment.AppointmentCancelView.as_view(), name= "cancel_appointment")
    
]
