from django.contrib import admin
from visitor.models import VisitorInfo


# Register your models here.
@admin.register(VisitorInfo)
class VisitorInfoAdmin(admin.ModelAdmin):
    list_display=('user','phone_no','national_id','designation')
    search_fields=('user','phone_number',)
    list_filter=('designation',)
    list_per_page=50
