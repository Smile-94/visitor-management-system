from django.db import models


#models
from accounts.models import User 

# Create your models here.
class VisitorInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='visitor_info')
    phone_no=models.CharField(max_length=15)
    national_id=models.CharField(max_length=20,blank=True)
    passport_no=models.CharField(max_length=30)
    occupation=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    organization=models.CharField(max_length=100,blank=True)
    organization_address=models.CharField(max_length=50,blank=True)
    bio=models.TextField(max_length=200,blank=True)

    def __str__(self):
        return str(self.user.email)

class VisitorMediaLink(models.Model):
    link_of = models.OneToOneField(User, on_delete=models.CASCADE, related_name='visitor_link')
    website = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.link_of)





    
