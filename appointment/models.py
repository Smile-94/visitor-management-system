from django.db import models
from datetime import datetime

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

    def __str__(self):
        return str(self.appointment_of)+str(self.appointment_date)


class AppointmentApplication(models.Model):
    appointment_of = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointment_from')
    request_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='request_by')
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issued_by')
    appointment_id= models.CharField(max_length=20, unique=True, blank=True, null=True)
    request_date = models.DateField(auto_now=False, auto_now_add=False)
    approved_date = models.DateField(auto_now=False, auto_now_add=False)
    heading = models.CharField(max_length=50)
    description = models.TextField()
    accept_status = models.BooleanField(default=False)
    meeting_time = models.TimeField(auto_now=False, auto_now_add=False,blank=True)
    message = models.TextField()
    decline_status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.appointment_id:
            year = str(datetime.date.today().year)[2:4]
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            self.appointment_id = 'E'+year+month+day+str(self.pk).zfill(4)
            self.save()
    
    def __str__(self):
        return str(self.request_by)
    
