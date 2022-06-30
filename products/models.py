from django.db import models
from kvapp.models import User
# Create your models here.

class Product(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    price = models.CharField(max_length=225)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    color = models.CharField(max_length=225)
    size = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=225, null=True, blank=True)
    weight = models.CharField(max_length=225,  null=True, blank=True)
    category1 = models.CharField(max_length=225)
    category2 = models.CharField(max_length=225)
    category3 = models.CharField(max_length=225, null=True, blank=True)
    category4 = models.CharField(max_length=225, null=True, blank=True)
    category5 = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name

