from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)

 
class Auto(models.Model):
    # COVERAGE_CHOICES=[
    #     ('NO COVERAGE CHANGES','No coverage changes'),
    #     ('SIMILAR COVERAGE WITH MIOR ADJUSTMENTS','Similar coverage with minor adjustments'),
    #     ('OPEN TO ANY ADJUSTMENTS','Open to any adjustments')
    # ]
    # CONDITION_CHOICES=[
    #     ('LIKE NEW','Like New'),
    #     ('MINOR COSMETIC ISSUES','Minor Cosmetic Issues'),
    #     ('MINOR MECHANICAL ISSUES','Minor Mechanical Issues'),
    #     ('MAJOR MECHANICAL ISSUES','Major Mechanical Issues')
    # ]
    # CREDIT_SCORE_CHOICES=[
    #     ('800+','800+'),
    #     ('720-800','720-800'),
    #     ('600-719','600-719'),
    #     ('400-599','400-599')
    # ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50, default=None)
    year = models.IntegerField(default=None)
    # condition = models.CharField(max_length=50,
    #     choices= CONDITION_CHOICES,
    #     default='LIKE NEW')
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
    zip = models.IntegerField(default=None)
    annual_miles = models.IntegerField(default=None)
    # # credit_score = models.CharField(max_length=10,
    # #     choices = CREDIT_SCORE_CHOICES,
    # #     default = '800+')
    credit_score = models.CharField(max_length=50, default=None)
    age = models.IntegerField(default=None)
    # # coverage_preference = models.CharField(max_length=100, 
    # #     choices = COVERAGE_CHOICES,
    # #     default='NO COVERAGE CHANGES') 
    coverage_preference = models.CharField(max_length=50, default=None)
    username = models.CharField(max_length=100, default=None)
    
    def __str__(self):
        return self.make
    
class Artist(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_artist = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']