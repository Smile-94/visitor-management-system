from django.urls import path

app_name = 'receptonist'

from receptonist.views import receptonist_main
from receptonist.views import manage_profile
from receptonist.views import manage_appointment
from receptonist.views import onarival_appointment


urlpatterns = [
    path('receptonist-home/', receptonist_main.ReceptonistHomeView.as_view(), name='receptonist'),
]

# Manage Profile
urlpatterns += [
    path('receptonist-profile/<int:pk>/', manage_profile.ReceptonistProfileView.as_view(), name='receptonist_profile'),
    path('receptonist-social-media/<int:pk>/', manage_profile.ReceptonistSocialMediaLinkView.as_view(), name='receptonist_social_media'),
    
]

# Manage Appointment
urlpatterns += [
    path('requested-appointment-list', manage_appointment.ReceptionAppointmentListView.as_view(), name='requested_appoinment_list' ),
    path('issued-appointment-list', manage_appointment.ReceptonistIssuedAppointmentListView.as_view(), name='issued_appoinment_list' ),
    path('receptonist-requested-appointment-detail/<int:pk>/', manage_appointment.ReceponistAppointmentDetailsView.as_view(), name='receptonist_appoinment_details' ),
    path('issued-appointment/<int:pk>/', manage_appointment.IssuedAppointmentView.as_view(), name='issued_appoinment' ),
    path('exit-appointment/<int:pk>/', manage_appointment.ExitIssuedAppointmentView.as_view(), name='exit_appoinment' ),
]

# On Arival Appointment
urlpatterns += [
    path('onarival-employee-list/', onarival_appointment.OnArivalAppointmentView.as_view(), name='onarival_employee_list'),
    path('onarival-appointment-list/', onarival_appointment.OnArivalAppointmentListView.as_view(), name='onarival_appointmetn_list'),
    path('onarival-appointment-exit/<int:pk>/', onarival_appointment.OnArivalAppointmentExitView.as_view(), name='onarival_appointmetn_exit'),
    path('onarival-appointment-deatails/<int:pk>/', onarival_appointment.OnArivalAppointmentDetailView.as_view(), name='onarival_appointmetn_details'),
]


