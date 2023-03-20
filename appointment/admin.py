from django.contrib import admin

# models
from appointment.models import Appointment
from appointment.models import AppointmentApplication

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_of','appointment_date','meet_from','meet_to','visiting_hour')
    search_fields = ('appointment_of','appointment_date')
    list_filter = ('is_active',)
    list_per_page = 50

@admin.register(AppointmentApplication)
class AppointmentApplicationAdmin(admin.ModelAdmin):
    list_display = ('request_by','issued_by','appointment_id','request_date')
    search_fields = ('request_by','appointment_id')
    list_per_page = 50
