from django.urls import path

app_name = 'receptonist'

from receptonist.views import receptonist_main
from receptonist.views import manage_profile


urlpatterns = [
    path('receptonist-home/', receptonist_main.ReceptonistHomeView.as_view(), name='receptonist'),
]

# Manage Profile
urlpatterns += [
    path('receptonist-profile/<int:pk>/', manage_profile.ReceptonistProfileView.as_view(), name='receptonist_profile'),
    path('receptonist-social-media/<int:pk>/', manage_profile.ReceptonistSocialMediaLinkView.as_view(), name='receptonist_social_media'),
    
]
