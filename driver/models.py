# from django.db import models
# import datetime as dt
# from django.contrib.auth.models import User
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # telephone = RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')



# # Create your models here.

# class Profile(models.Model):
#     car = models.OneToOneField(Car)
#     location = models.ForeignKey(Location)
#     destination = models.ForeignKey(Location)
#     name = models.CharField(max_length=60)
#     profile_avatar = ProcessedImageField(upload_to = 'avatars/', processors=[ResizeToFill(100,100)], format = 'JPEG', options ={'quality':60})
#     date = models.DateTimeField(auto_now_add=True)
#     # number = models.CharField(max_length=10,validators=[telephone, MaxLengthValidator])

#     def save_profile(self):
#         self.save()
    
#     def delete_profile(self):
#         self.delete()
#     @classmethod 
#     def search_profile(cls,name):
#         return cls.objects.filter(name__name=name)
    
    
#     @classmethod
#     def get_all(cls):
#         profiles = Profile.objects.all()
#         return profiles

#     @receiver(post_save,sender=User)
#     def update_profile(sender,instance,created,**kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#         instance.profile.save()

# class Car(models.Model):
#     number_plate = models.CharField(max_length=12)
#     brand = models.CharField(max_length=30)
#     number_of_seats = models.IntegerField(max_length=10)
#     driver = models.OneToOneField(Profile)
#     time = models.DateTimeField(auto_now_add=True)

#     def save_car(self):
#         self.save()
    
#     def delete_car(self):
#         self.delete()


# class Location(models.Model):
#     name = models.ForeignKey(Profile)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     time = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-time']
#     def __str__(self):
#         return self.name

#     def save_locations(self):
#         self.save()