from django.urls import path

app_name ='report'

from report.views import generate_pdf

urlpatterns = [
    path('visitor-profile/<int:pk>/', generate_pdf.VisittorProvilePdfView.as_view(), name='visitor_profile'),
    path('employee-profile/<int:pk>/', generate_pdf.EmployeeProfileView.as_view(), name='employee_profile'),
    path('appointment-report/<int:pk>/', generate_pdf.AppointmentDetailsPdf.as_view(), name='appointment_report'),
    path('onarival-appointment-report/<int:pk>/', generate_pdf.OnArivalAppointmentPdf.as_view(), name='onarivla_appointment_report'),
]
