from django.contrib import admin

# Models
from employee.models import EmployeeInfo
from employee.models import SocialMediaLink

# Register your models here.
@admin.register(EmployeeInfo)
class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display=('info_of', 'position','employee_id', 'joining_date', 'is_active')
    search_fields=('info_of', 'phone',)
    list_filter=('position',)
    list_per_page=50

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('link_of',)
