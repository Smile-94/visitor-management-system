from django.urls import path

app_name = 'receptonist'

from receptonist.views import receptonist_main
from receptonist.views import manage

urlpatterns = [
    path('receptonist-home/', receptonist_main.ReceptonistHomeView.as_view(), name='receptonist'),
]

# Manage Profile
urlpatterns += [
    path('receptonist-profile/', manage_profile.)
]
