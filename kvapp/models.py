from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    pass

class Product(models.Model):
    pass

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=225, unique=True, null=True, blank=True)
    username = models.CharField(max_length=225)
    phone  = models.CharField(null=True, max_length=225, blank=True)
    vendor = models.BooleanField(default=False)
    shop_name = models.CharField(max_length=225, default='#', null=True, blank=True)
    shop_url = models.URLField(max_length=1000, default='#', null=True, blank=True)
    REQUIRED_FIELDS =  ['username']
    USERNAME_FIELD = 'email'


    def get_username(self):
        return self.username