from django.db import models
from django.conf import settings

# Models
from accounts.models import User

# Create your models here.
class Appointment(models.Model):
    appointment_of=models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointment_user")
    appointment_date=models.DateField(auto_now=False, auto_now_add=False)
    meet_from=models.TimeField(auto_now=False, auto_now_add=False)
    meet_to=models.TimeField(auto_now=False, auto_now_add=False)
    is_active=models.BooleanField(default=True)
    cancel_status=models.BooleanField(default=False)
    cancel_message=models.CharField(max_length=200,blank=True,null=True)
