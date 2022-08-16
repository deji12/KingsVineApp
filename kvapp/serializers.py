from rest_framework import serializers
from rest_framework.response import Response
# from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
from django.contrib.auth import authenticate
from rest_framework import status

class UpdateUserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ['password']

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'phone', 'shop_name', 'shop_url', 'phone')

    # def validate(self, attrs):
    #     if len(attrs['password']) < 8:
    #         raise serializers.ValidationError({'Error': 'Password too short'})

class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
