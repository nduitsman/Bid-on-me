from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Auto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50, default=None)
    year = models.IntegerField(default=None)
    condition = models.CharField(max_length=50, default=None)
    mileage = models.CharField(max_length=50, default=None)
    accidents = models.BooleanField(default=False)
    tickets = models.BooleanField(default=False)
    premium = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    provider = models.CharField(max_length=50, default=None)
    liability = models.CharField(max_length=50, default=None)
    uninsured = models.CharField(max_length=50, default=None)
    medical = models.IntegerField(default=None)
    roadside = models.BooleanField(default=False)
    rental = models.BooleanField(default=False)
    safe_driver = models.BooleanField(default=False)
    zip = models.CharField(max_length=5,default=None)
    annual_miles = models.IntegerField(default=None)
    credit_score = models.CharField(max_length=50, default=None)
    age = models.IntegerField(default=None)
    coverage_preference = models.CharField(max_length=50, default=None)
    username = models.CharField(max_length=100, default=None)
    
    def __str__(self):
        return self.make
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50, default=1)
    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
