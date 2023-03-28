from django.urls import path

#Views
from visitor.views import visitor_main
from visitor.views import manage_profile
from visitor.views import manage_appointment

app_name='visitor'

urlpatterns = [
    path('visitor-home/', visitor_main.VisitorHomeView.as_view(), name='visitor_home'),
]


urlpatterns += [
    path('profile/<int:pk>/', manage_profile.VisitorProfileView.as_view(), name='profile'),
    path('edit-visitor-profile/<int:pk>/', manage_profile.EditProfileView.as_view(), name='edit_profile'),
    path('edit-address/<int:pk>/', manage_profile.EditAddressView.as_view(), name='edit_address'),
    path('edit-media-link/<int:pk>/', manage_profile.UpdateMediaLinkView.as_view(), name='edit_media_link'),
]

# Manage Appointment
urlpatterns += [
    path('appointment-application/<int:pk>/', manage_appointment.TakeAppointmentView.as_view(), name='take_appointment'),
    path('pending-appointment-list/', manage_appointment.PendingAppointmentListView.as_view(), name='pending_appointment_list'),
    path('accpted-appointment-list/', manage_appointment.AccptedAppointmentListView.as_view(), name='accpted_appointment_list'),
    path('declined-appointment-list/', manage_appointment.DeclinedAppointmentListView.as_view(), name='declined_appointment_list'),
    path('cancel-appointment-list/', manage_appointment.CancelAppointmentListView.as_view(), name='cancel_appointment_list'),
    path('visitor-appointment-details/<int:pk>/', manage_appointment.AppointmentDetailsView.as_view(), name='visitor_appointment_details'),
]

