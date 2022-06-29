from rest_framework import serializers
from . import models
from kvapp.models import User
from .models import ShippingAddress

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShippingAddress
        fields = '__all__'

class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BillingAddress
        fields = '__all__'