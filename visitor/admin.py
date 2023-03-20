from django.contrib import admin
from visitor.models import VisitorInfo
from visitor.models import VisitorMediaLink


# Register your models here.
@admin.register(VisitorInfo)
class VisitorInfoAdmin(admin.ModelAdmin):
    list_display=('user','phone_no','national_id','designation')
    search_fields=('user','phone_number',)
    list_filter=('designation',)
    list_per_page=50

@admin.register(VisitorMediaLink)
class VisitorMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('link_of',)