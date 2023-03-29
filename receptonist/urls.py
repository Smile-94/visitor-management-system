from django.urls import path

app_name = 'receptonist'

from receptonist.views import receptonist_main
from receptonist.views import manage_profile
from receptonist.views import manage_appointment


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
    path('requested-appointment-detail/<int:pk>/', manage_appointment.ReceponistAppointmentDetailsView.as_view(), name='receptonist_appoinment_details' ),
    path('issued-appointment/<int:pk>/', manage_appointment.IssuedAppointmentView.as_view(), name='issued_appoinment' ),
]

