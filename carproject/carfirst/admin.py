from django.contrib import admin
from carfirst.models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_listview=('username','place_name','date','phone_no','number_of_passenger','vehicle_required')
admin.site.register(Notification,NotificationAdmin)
# Register your models here.
