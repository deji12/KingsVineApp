from django.db import models
from kvapp.models import User

# Create your models here.

class ShippingAddress(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    company_name = models.CharField(max_length=300, null=True,blank=True)
    country = models.CharField(max_length=225)
    street_address1 = models.TextField()
    street_address2 = models.TextField(null=True,blank=True)
    town_city = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    postcode_zip = models.CharField(max_length=225)
    
    def __str__(self):
        return str(self.user)


class BillingAddress(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    company_name = models.CharField(max_length=300, null=True,blank=True)
    country = models.CharField(max_length=225)
    street_address1 = models.TextField()
    street_address2 = models.TextField(null=True,blank=True)
    town_city = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    postcode_zip = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    email= models.EmailField()
    
    def __str__(self):
        return str(self.user)