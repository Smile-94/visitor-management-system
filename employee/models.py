from django.db import models
import datetime

# models
from accounts.models import User

# Image upload directory path
from employee.utils import user_directory_path

# Image validator
from employee.utils import validate_image_type
from employee.utils import validate_image_dimention
from employee.utils import validate_image_signature_dimention
from employee.utils import validate_image_file_size
from employee.utils import validate_signature_image_file_size


DEPARTMENT_OPT = (
    ('HR', 'Human Resource'),
    ('administrative', 'Administrative'),
    ('software development', 'Software Development'),
    ('QA', 'Quality Assurance'),
    ('project management', 'Project Management'),
    ('Product Management', 'Product Management'),
    ('design', 'Design'),
    ('devOps', 'DevOps'),
    ('customer support', 'Customer Support'),
    ('marketing', 'Marketing'),
    ('IT', 'Information Technology')
)


class DesignationInfo(models.Model):
    designation = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT_OPT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.designation}, {self.department}"


# Create your models here.
class EmployeeInfo(models.Model):
    info_of = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_info')
    position = models.ForeignKey(DesignationInfo, on_delete=models.SET_NULL, blank=True, null=True)
    employee_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    joining_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=15)
    national_id = models.CharField(max_length=50)
    passport_no = models.CharField(max_length=50, blank=True, null=True)
    driving_license = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to=user_directory_path )
    signature = models.ImageField(upload_to=user_directory_path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.employee_id:
            year = str(datetime.date.today().year)[2:4]
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            self.employee_id = 'E'+year+month+day+str(self.pk).zfill(4)
            self.save()
    

    def __str__(self):
        return str(f"{self.info_of}'s Info")

class SocialMediaLink(models.Model):
    link_of = models.OneToOneField(User, on_delete=models.CASCADE, related_name='media_link')
    twitter = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)

    def __str__(self):
        return str(self.link_of)

class Review(models.Model):
    RATING_CHOICES = (
        (1, 'Poor(1)'),
        (2, 'Fair(2)'),
        (3, 'Good(3)'),
        (4, 'Very Good(4)'),
        (5, 'Excellent(5)')
    )
    review_of = models.ForeignKey(User,on_delete=models.CASCADE,related_name='review_of')
    review_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'review_by')
    rating = models.IntegerField(choices=RATING_CHOICES)
    subject = models.CharField(max_length=100)
    review_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


