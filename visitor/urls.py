from django.urls import path

#Views
from visitor.views import visitor_main
from visitor.views import manage_profile

app_name='visitor'

urlpatterns = [
    path('visitor-home/', visitor_main.VisitorHomeView.as_view(), name='visitor_home'),
]


urlpatterns += [
    
    path('profile/<int:pk>/', manage_profile.VisitorProfileView.as_view(), name='profile'),
    path('edit-visitor-profile/<int:pk>/', manage_profile.EditProfileView.as_view(), name='edit_profile'),
    path('edit-address/<int:pk>/', manage_profile.EditAddressView.as_view(), name='edit_address'),
]
