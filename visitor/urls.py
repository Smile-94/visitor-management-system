from django.urls import path

#Views
from visitor.views import VisitorHome
from visitor.views import VisitorProfile
from visitor.views import EditProfileView
from visitor.views import EditAddressView

app_name='visitor'

urlpatterns = [
    path('visitor-home/', VisitorHome.as_view(), name='visitor_home'),
    path('profile/<int:pk>/', VisitorProfile.as_view(), name='profile'),
    path('edit-visitor-profile/<int:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('edit-address/<int:pk>/', EditAddressView.as_view(), name='edit_address'),
]
