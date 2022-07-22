from rest_framework import serializers
from .models import Store

class StoreSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'