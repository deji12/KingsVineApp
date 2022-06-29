from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from .serializers import UpdateUserPasswordSerializer, UpdateUserProfileSerializer
from .serializers import AllUsersSerializer
from kvapp import serializers


@api_view(['GET'])    
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data='Only for logged in user',status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_users (request):
    users = User.objects.all()
    serializer = AllUsersSerializer(users,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateUserPassword(request):
    if request.method == 'POST':
        get_user = User.objects.get(email=request.user)
        data = {}
        if request.data.get('password'):
            data['password'] = request.data.get('password')
            

        serializer = UpdateUserPasswordSerializer(data=data, context={'request': request, 'dataa': data})
        if serializer.is_valid():
            authenticate_user = authenticate(email=get_user.email, password=request.data['password'])
            if authenticate_user is not None:
                if request.data.get('newpassword') != request.data.get('confirmpassword'):
                    return Response({'Error':  'Create and confirm passwords do not match'})
                else:
                    get_user.set_password(request.data['confirmpassword'])
                    get_user.save()
                    return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/auth/token/logout/')
                    # return Response(data='Password successfully updated')
                    
            else:
                return Response({'Error': 'Old password is not correct'})
        else:
            data = serializer.errors
            return Response(data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateUserProfile(request):
    get_user = User.objects.get(email=request.user)
    if request.method  == 'PUT':
        data = {}
        if request.data.get('username'):
            data['username'] = request.data.get('username')
        if request.data.get('first_name'):
            data['first_name'] = request.data.get('first_name')
        if request.data.get('last_name'):
            data['last_name'] = request.data.get('last_name')
        if request.data.get('email'):
            data['email'] = request.data.get('email')
        if request.data.get('phone'):
            data['phone'] = request.data.get('phone')

        serializer = UpdateUserProfileSerializer(data=data)
        if serializer.is_valid():
            if request.data.get('username'):
                get_user.username = request.data.get('username')
                get_user.save()
            if request.data.get('first_name'):
                get_user.first_name = request.data.get('first_name')
                get_user.save()
            if request.data.get('last_name'):
                get_user.last_name = request.data.get('last_name')
                get_user.save()
            if request.data.get('email'):
                get_user.email = request.data.get('email')
                get_user.save()
            if request.data.get('phone'):
                get_user.phone = request.data.get('phone')
                get_user.save()
        else:
            data = serializer.errors
            return Response(data)
        return Response(data='Account successfully updated')

