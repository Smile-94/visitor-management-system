from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject= models.CharField(max_length=100)
    message= models.TextField()

    def __str__(self):
        return str(f" {{self.name}}'message ")