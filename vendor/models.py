from django.db import models
from kvapp.models import User

# Create your models here.
class Store(models.Model):
    vendor_name = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=225, null=True, blank=True)
    store_products_per_page = models.IntegerField(default=10, null=True, blank=True)
    store_banner = models.FileField(upload_to='StoreBanner', null=True, blank=True)
    profile_picture = models.FileField(upload_to='ProfilePicture', null=True, blank=True)
    street = models.CharField(max_length=500, null=True, blank=True)
    street2 = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    show_email_address = models.BooleanField(default=True)
    post_zip_code = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.vendor_name)

class PaymentSetup(models.Model):
    vendor_name = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_account_name = models.CharField(max_length=500)
    bank_account_number = models.CharField(max_length=500)
    bank_name = models.CharField(max_length=500)
    bank_address = models.TextField()
    routing_number = models.CharField(max_length=225)
    iban = models.CharField(max_length=225)
    swift_code = models.CharField(max_length=225)

    def __str__(self):
        return str(self.vendor_name)