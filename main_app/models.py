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
    # bid_count = models.IntegerField(default=None)
    
    def __str__(self):
        return self.make
class Bid(models.Model):
    auto_post_id = models.IntegerField(default=None)
    username = models.CharField(max_length=150, default=None)
    company = models.CharField(max_length=150, default=None)
    phone_number = models.CharField(max_length=150, default=None)
    more_info = models.TextField(max_length=1000, default=None)
    def __str__(self):
        return self.company
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length = 100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    profile_image = models.CharField(max_length=250, blank=True)
    company = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
