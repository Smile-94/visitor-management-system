from django.urls import path

app_name ='report'

from report.views import generate_pdf

urlpatterns = [
    path('visitor-profile/<int:pk>/', generate_pdf.VisittorProvilePdfView.as_view(), name='visitor_profile')
]
