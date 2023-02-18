from django.contrib import admin

# models
from home.models import ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject')
    search_fields = ('name',)
    list_per_page = 50
