from django.db import models
from products.models import Product
from Customers.models import BillingAddress, ShippingAddress
from kvapp.models import User


class OrderModel(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_vendor = models.ForeignKey(User, related_name='product_vendor', on_delete=models.CASCADE, null=True, blank=True)
    product_price = models.IntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    customer = models.ForeignKey(User, related_name='product_customer', on_delete=models.CASCADE, null=True, blank=True)
    customer_billing_address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE, null=True, blank=True)
    customer_shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, null=True, blank=True)
    ipn_valid = models.BooleanField(default=False, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product_name)

