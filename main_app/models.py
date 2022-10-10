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
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    # condition = models.CharField(max_length=50,
    #     choices= CONDITION_CHOICES,
    #     default='LIKE NEW')
    condition = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)
    accidents = models.BooleanField(default=False)
    tickets = models.BooleanField(default=False)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.CharField(max_length=50)
    liability = models.CharField(max_length=50)
    uninsured = models.CharField(max_length=50)
    medical = models.IntegerField()
    roadside = models.BooleanField(default=False)
    rental = models.BooleanField(default=False)
    safe_driver = models.BooleanField(default=False)
    zip = models.IntegerField()
    annual_miles = models.IntegerField()
    # credit_score = models.CharField(max_length=10,
    #     choices = CREDIT_SCORE_CHOICES,
    #     default = '800+')
    credit_score = models.CharField(max_length=50)
    age = models.IntegerField()
    # coverage_preference = models.CharField(max_length=100, 
    #     choices = COVERAGE_CHOICES,
    #     default='NO COVERAGE CHANGES') 
    coverage_preference = models.CharField(max_length=50)
    
    def __str__(self):
        return self.make
    