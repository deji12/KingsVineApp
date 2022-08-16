from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User, UserLoginCode
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from .serializers import UpdateUserPasswordSerializer, UpdateUserProfileSerializer,UserCreateSerializer
from .serializers import AllUsersSerializer
from kvapp import serializers
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import datetime
import random
from datetime import timedelta

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
def CreateUser(request):
    if request.method == 'POST':
        serializer =  UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            if len(request.data.get('password')) < 8:
                return Response({'Error': 'Passwords is too short'})
            if request.data.get('password') == request.data.get('confirm_password'):
                user = User.objects.create_user(
                    username=request.data.get('username'),
                    email=request.data.get('email'),
                    first_name= request.data.get('first_name'),
                    last_name = request.data.get('last_name'),
                    password= request.data.get('password'),
                )
                if request.data.get('shop_url'):
                    user.shop_url = request.data.get('shop_url')

                if request.data.get('shop_name'):
                    user.shop_name = request.data.get('shop_name')

                if request.data.get('phone'):
                    user.phone = request.data.get('phone')

                if request.data.get('role') == 'customer':
                    user.vendor = False
                else:
                    user.vendor = True   
                user.save()
                return Response(data='User Created Successfully')
            else:
                return Response({'Error': 'Passwords do not match'})
        else:
            data = serializer.errors
            return Response(data)

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
                    return HttpResponseRedirect(redirect_to='https://kvappdj.herokuapp.com/auth/token/logout/')
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

@api_view(['POST', 'GET'])
def ForgotPassword(request):
    if request.method == 'POST':
        # getting user inputs from frontend
        email = request.data.get('email')

        user = User.objects.get(email=email) # get user

        # validate email
        check_if_email_exists = User.objects.filter(email=email)
        if check_if_email_exists:

            numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            login_code = ''
            while len(login_code) < 6:
                new_value = random.choice(numbers)
                login_code += new_value

            # add an expiration time to code used to reset password
            t1 = datetime.datetime.now() #current time
            t2 = timedelta(minutes=10) # time required to reset password
            expiration_time = t1+t2 # final expiration time

            new_login_code = UserLoginCode(user=user, code=login_code, expiration=expiration_time)
            new_login_code.save()

            email_template_name = 'kvapp/forgot_email.html'
            context = {
                'username': user.username,
                'code': login_code,
            }
            email_body = render_to_string(email_template_name, context)     

            email_mess = EmailMessage (
                'Reset Your Password: Acorn', # email subject
                email_body, # email content
                settings.EMAIL_HOST_USER, # email sender
                [email] # recipients
            )
            email_mess.fail_silently = True
            email_mess.content_subtype = 'html'
            email_mess.send()

            return Response(data=f'Password Reset Successful')
        else:
            return Response(data=f'No user with email {email} exists')

    # return render(request, 'AuthenticationApp/forgot_password.html')

#reset password email 
@api_view(['POST'])
def ResetPasswordView(request, username, code):
    if request.method == 'POST':
        get_user = User.objects.get(username=username)
        get_code = UserLoginCode.objects.get(user=get_user, code=code)
        # getting user inputs from frontend
        password = request.data.get('password')
        confirm_password = request.data.get('verifyPassword')

        # validate passwords
        if len(password) < 5:
            return Response(data='Passwords cannot be less than 5 characters')

        if password != confirm_password:
            return Response(data='Passwords do not match, try again')

        #check if code is still valid
        expiration_date = get_code.expiration
        year = expiration_date.split('-')[0]
        month = expiration_date.split('-')[1].strip('0')
        split_to_two = expiration_date.split(' ')[1]
        split_for_date = expiration_date.split(' ')[0]
        day = split_for_date.split('-')[2]
        hour = split_to_two.split(':')[0]
      
        minute = split_to_two.split(':')[1]

        code_expiration_date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
        current_time = datetime.datetime.now()

        #if link has expired
        if current_time > code_expiration_date:
            get_code.delete() # delete code after use
            return Response(data='This link has expired. Proceed to the forgot password reset page to get another link.')

        #save password is link is still valid
        else:
            #save new password after validation
            get_user.set_password(confirm_password)
            get_user.save()
            get_code.delete() # delete code after use
            # redirect to login page after password reset
            return Response(data='Password successfully changed. Login now')

    # return render(request, 'AuthenticationApp/reset_password.html')