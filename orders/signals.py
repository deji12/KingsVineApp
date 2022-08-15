from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from orders.models import OrderModel
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404
from kvapp.models import User
from products.models import Product

@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    print('ipn valid')
    ipn = sender
    if ipn.payment_status =='Completed':
        get_order = get_object_or_404(OrderModel, id=ipn.invoice)
        get_order.ipn_valid = True
        get_order.save()

@receiver(invalid_ipn_received)
def invalid_ipn_signal(sender, **kwargs):
    print('ipn invalid')
    ipn = sender
    if ipn.payment_status =='Completed':
        get_order = get_object_or_404(OrderModel, id=ipn.invoice)
        get_order.ipn_valid = False
        get_order.save()

