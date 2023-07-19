from django.contrib import admin
from .models import Members,Events,WeeklyDevotion,Gallery
# Register your models here.
@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display=["firstname","lastname","phonenumber","county"]
    
admin.site.register(Gallery)
admin.site.register(Events)
admin.site.register(WeeklyDevotion)