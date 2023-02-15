from django.urls import path

# view from home app views.py
from home.views import Home

app_name = 'home'

urlpatterns = [

    path('', Home.as_view(), name='index')
    
]
