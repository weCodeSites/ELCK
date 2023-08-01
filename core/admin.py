from django.contrib import admin
from .models import Members,Events,WeeklyDevotion,Gallery,Sermon
# Register your models here.
@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display=["firstname","lastname","phonenumber","county","college"]
    
admin.site.register(Gallery)
admin.site.register(Events)
admin.site.register(WeeklyDevotion)
admin.site.register(Sermon)