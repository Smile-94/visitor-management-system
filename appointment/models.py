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
    entering_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    exit_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    duration = models.DurationField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    

    def save(self, *args, **kwargs):
        if not self.appointment_id:
            self.pk = None
            year = str(date.today().year)[2:4]
            month = str(date.today().month)
            day = str(date.today().day)
            self.appointment_id = 'A'+year+month+day+str(self.pk).zfill(4)

        if self.entering_time and self.exit_time:
            duration = datetime.combine(datetime.today(), self.exit_time) - datetime.combine(datetime.today(), self.entering_time)
            self.duration = duration

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.request_by)

class OnArivalAppointmentApplication(models.Model):
    appointment_to = models.ForeignKey(User,on_delete=models.CASCADE, related_name='onarival_appointment')
    request_by = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    national_id = models.CharField(max_length=20)
    appointment_date = models.DateField(auto_now_add=True, null=True)
    phone_no = models.CharField(max_length=15)
    email_id = models.EmailField(max_length=254, blank=True, null=True)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='onarival_issued_by', blank=True, null=True)
    appointment_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    issued_status = models.BooleanField(default=False)
    entering_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    exit_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    duration = models.DurationField(blank=True, null=True)
    photo = models.ImageField(upload_to='appointment/', null=True)
    is_active = models.BooleanField(default=True)
    

    def save(self, *args, **kwargs):
        if not self.appointment_id:
            self.pk = None  # Set the primary key to None so that a new one is assigned
            super().save(*args, **kwargs)  # Save the object to generate a primary key
            year = str(date.today().year)[2:4]
            month = str(date.today().month)
            day = str(date.today().day)
            self.appointment_id = 'OA' + year + month + day + str(self.pk).zfill(4)

        if self.entering_time and self.exit_time:
            duration = datetime.combine(datetime.today(), self.exit_time) - datetime.combine(datetime.today(), self.entering_time)
            self.duration = duration

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.request_by)