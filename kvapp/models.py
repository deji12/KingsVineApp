from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    pass

class Product(models.Model):
    pass

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=225, unique=True, null=True, blank=True)
    phone  = models.CharField(null=True, max_length=225, blank=True)
    vendor = models.BooleanField(default=False)
    REQUIRED_FIELDS =  [ 'phone', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'


    def get_username(self):
        return self.email