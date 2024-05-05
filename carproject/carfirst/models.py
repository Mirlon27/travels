from django.db import models

# Create your models here.
class Notification(models.Model):
    username = models.CharField(max_length=100)
    place_name = models.CharField(max_length=300)
    date = models.DateField()
    phone_no = models.IntegerField(max_length=10)
    number_of_passenger = models.IntegerField(max_length=50)
    vehicle_required = models.CharField(max_length=100)

