from django.db import models
from datetime import datetime
from datetime import date

# Models
from accounts.models import User

# Create your models here.
class Appointment(models.Model):
    appointment_of=models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointment_user")
    appointment_date=models.DateField(auto_now=False, auto_now_add=False)
    meet_from=models.TimeField(auto_now=False, auto_now_add=False)
    meet_to=models.TimeField(auto_now=False, auto_now_add=False)
    visiting_hour = models.DurationField(blank=True, null=True)
    is_active=models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        from_time = datetime.combine(datetime.today(), self.meet_from)
        to_time = datetime.combine(datetime.today(), self.meet_to)
        duration = to_time - from_time
        self.visiting_hour = duration
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.appointment_of)+str(self.appointment_date)


class AppointmentApplication(models.Model):
    appointment_of = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointment_from')
    request_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='request_by')
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='issued_by', blank=True, null=True)
    appointment_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    request_date = models.DateField(auto_now_add=True)
    approved_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    heading = models.CharField(max_length=100)
    description = models.TextField()
    issued_status = models.BooleanField(default=False)
    accept_status = models.BooleanField(default=False)
    meeting_time = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    message = models.TextField()
    decline_status = models.BooleanField(default=False)
    cancel_status = models.BooleanField(default=False)
    cancel_message = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.appointment_id:
            year = str(date.today().year)[2:4]
            month = str(date.today().month)
            day = str(date.today().day)
            self.appointment_id = 'E'+year+month+day+str(self.pk).zfill(4)
            self.save()
    
    def __str__(self):
        return str(self.request_by)
    
