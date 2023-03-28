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
    path('employee-profile-details/<int:pk>/', manage_profile.EmployeeProfileView.as_view(), name='employee_profile_details'),
    path('add-update-social-media-link/<int:pk>/', manage_profile.EmployeeSocialMediaLinkView.as_view(), name='add_update_social_media_link')
    
]


# add, update, delete appointment
urlpatterns += [
    path('add_appointment/', employee_aapointment.AppointmentView.as_view(), name= "add_appointment"),
    path('update-appointment/<int:pk>/', employee_aapointment.AppointmentUpdateView.as_view(), name= "update_appointment"),
    path('delete-appointment/<int:pk>/', employee_aapointment.DeleteAppointmentView.as_view(), name= "delete_appointment"),

    # Appointment Application
    path('employee-pending-application-list/', employee_aapointment.EmployeePendingAppointmentView.as_view(), name= "employee_pending_application_list"),
    path('employee-accepted-application-list/', employee_aapointment.EmployeeAcceptedApointmentListView.as_view(), name= "employee_accepted_application_list"),
    path('employee-declined-application-list/', employee_aapointment.DeclinedAppointmentListView.as_view(), name= "employee_declined_application_list"),
    path('employee-cancel-application-list/', employee_aapointment.CancelAppointmentListView.as_view(), name= "employee_cancel_application_list"),
    path('employee-accept-appointment/<int:pk>/', employee_aapointment.AcceptAppointmentView.as_view(), name= "employee_accept_appointment"),
    path('employee-decline-appointment/<int:pk>/', employee_aapointment.DeclineAppointmentView.as_view(), name= "employee_decline_appointment"),
    path('employee-cancel-appointment/<int:pk>/', employee_aapointment.CancelAppointmentView.as_view(), name= "employee_cancel_appointment"),
    path('employee-appointment-details/<int:pk>/', employee_aapointment.EmployeeAppointmentDetailsView.as_view(), name= "employee_appointment_details"),
    path('appointment-visitor-profile/<int:pk>/', employee_aapointment.AppointmentVisitorProfileView.as_view(),name='appointment_visitor_profile')
    
]
