from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from kvapp.models import User
from .serializers import ShippingAddressSerializer, BillingAddressSerializer
from .models import BillingAddress, ShippingAddress


# VIEW FOR SAVING USER SHIPPING DETAILS
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateShippingAddress(request):
    if request.method == 'POST':
        get_user = User.objects.get(username=request.data['user'])
        data = {
            'user': get_user.pk,
            'first_name': request.data['first_name'],
            'last_name': request.data['last_name'],
            'company_name': request.data['company_name'],
            'country': request.data['country'],
            'street_address1': request.data['street_address1'],
            'street_address2': request.data['street_address2'],
            'town_city': request.data['town_city'],
            'state': request.data['state'],
            'postcode_zip': request.data['postcode_zip']
            }
        serializer = ShippingAddressSerializer(data=data)
        data_response = {}
        if serializer.is_valid():
            serializer.save()
            return Response(data='Shipping address saved successfully')
        else:
            data = serializer.errors
            return Response(data_response)


# VIEW FOR VIEWING USER SHIPPING DETAIL
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewUserShippingAddress(request):
    get_user = User.objects.get(email=request.user)
    get_shipping_address = ShippingAddress.objects.get(user=get_user)
    serializer = ShippingAddressSerializer(get_shipping_address)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateBillingAddress(request):
    if request.method == 'POST':
        get_user = User.objects.get(username=request.data['user'])
        data = {
            'user': get_user.pk,
            'first_name': request.data['first_name'],
            'last_name': request.data['last_name'],
            'company_name': request.data['company_name'],
            'country': request.data['country'],
            'street_address1': request.data['street_address1'],
            'street_address2': request.data['street_address2'],
            'town_city': request.data['town_city'],
            'state': request.data['state'],
            'postcode_zip': request.data['postcode_zip'],
            'phone': request.data['phone'],
            'email': request.data['email']
            }
        serializer = BillingAddressSerializer(data=data)
        data_response = {}
        if serializer.is_valid():
            serializer.save()
            return Response(data='Billing address saved successfully')
        else:
            data_response = serializer.errors
            return Response(data_response)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewUserBillingAddress(request):
    get_user = User.objects.get(email=request.user)
    get_billing_address = BillingAddress.objects.get(user=get_user)
    serializer = BillingAddressSerializer(get_billing_address)
    return Response(serializer.data)