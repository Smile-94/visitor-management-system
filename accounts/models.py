from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy



# uploaded file path
from accounts.utils import user_directory_path

# Create your models here.
class MyUserManager(BaseUserManager):

    """A custom manager to deal with emails and custom identifiers"""

    def _create_user(self,email,password,**extra_fields):
        """A custom manager to deal with emails and custom identifiers"""
        if not email:
            raise ValueError('Users must have an email address')
        
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_emplyee(self,email,password,**extra_fields):
        user=self._create_user(email,password,**extra_fields)

        user.is_emplyee=True
        user.save(using=self._db)
        return user
    
    def create_visitor(self,email,password,**extra_fields):
        user=self._create_user(email,password,**extra_fields)

        user.is_visitor = True
        user.save(using=self._db)
        return user
    
    def create_receptonist(self,email,password,**extra_fields):
        user=self._create_user(email,password,**extra_fields)

        user.is_receptonist = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("usperuser must have is_staff=True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        return self._create_user(email,password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True,null=False)
    is_employee=models.BooleanField(default=False)
    is_visitor=models.BooleanField(default=False)
    is_receptonist = models.BooleanField(default= False)
    is_staff=models.BooleanField(
        gettext_lazy('staff_status'),default=False,
        help_text=gettext_lazy('designets wheter the user can loing to this site'),
    )

    is_active=models.BooleanField(
        gettext_lazy('active'),default=True,
        help_text=gettext_lazy('designets wheter the user can loin to this site'),
    )

    USERNAME_FIELD='email'

    objects=MyUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

# profile models gender choices
GENDER_OPT=(
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name=models.CharField(max_length=264,blank=True)
    last_name=models.CharField(max_length=15,blank=True)
    gender=models.CharField(max_length=10,choices=GENDER_OPT)
    photo=models.ImageField( upload_to=user_directory_path, null=True,default='default/user.jpg')
    date_of_join=models.DateField(auto_now_add=True)                                      

    def __str__(self):
        return self.first_name+"'s profile"

class PresentAddress(models.Model):
    address_of=models.OneToOneField(User,on_delete=models.CASCADE, related_name='present_address')
    road=models.CharField(max_length=50)
    sector=models.CharField( max_length=50)
    police_station=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    post_code=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.address_of}'s Present Address"

class PermanentAddress(models.Model):
    address_of=models.OneToOneField(User, on_delete=models.CASCADE,related_name='permanent_address')
    village=models.CharField(max_length=50)
    post_office=models.CharField(max_length=50)
    upzila=models.CharField(max_length=50)
    division=models.CharField(max_length=50)
    permanent_district=models.CharField(max_length=50)
    zip_code=models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.address_of}'s Parmanent Address"

