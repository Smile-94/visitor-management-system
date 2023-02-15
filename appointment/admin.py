from django.contrib import admin

# models
from appointment.models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_of','appointment_date','meet_from','meet_to')
    search_fields = ('appointment_of','appointment_date')
    list_filter = ('is_active',)
    list_per_page = 50
