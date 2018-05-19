from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from imagekit.models import ProccessedImageField
from imagekit.processors import ResizeToFill
telephone = RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')

# Create your models here.
class Profile(models.Model):
    car = models.OneToOneField(Car)
    location = models.ForeignKey(Location)
    destination = models.ForeignKey(Location)
    name = models.CharField(max_length=60)
    profile_avatar = ProccessedImageField(upload_to = 'avatars/', processors=[ResizeToFill(100,100)], format = 'JPEG', options ={'quality':60})
    date = models.DateTimeField(auto_now_add=True)
    number = models.CharField(max_length=10,validators=[telephone, MaxLengthValidator])

class Car(models.Model):
    number_plate = models.CharField(max_length=12)
    brand = models.CharField(max_length=30)
    number_of_seats = models.IntegerField(max_length=10)