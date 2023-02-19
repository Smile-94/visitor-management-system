from django.urls import path

# view from home app views.py
from home.views import home_view

app_name = 'home'

urlpatterns = [

    path('', home_view.HomveView.as_view(), name='index'),
    path('contact-message/', home_view.ContactMessageView.as_view(), name='contact_message'),
    
]
