from django.shortcuts import render
from requests import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import StoreSerilaizer
from kvapp.models import User
from .models import Store
# Create your views here.

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateStore(request):
    get_user = User.objects.get(email=request.user.email)
    store = Store.objects.get(vendor=get_user)

    data_context = {
        'vendor': get_user.pk,
    }

    if request.data.get('store_name'):
        data_context['store_name'] = request.data.get('store_name')
    if request.data.get('store_products_per_page'):
        data_context['store_products_per_page'] = request.data.get('store_products_per_page')
    if request.data.get('store_banner'):
        data_context['store_banner'] = request.data.get('store_banner')
    if request.data.get('profile_picture'):
        data_context['profile_picture'] = request.data.get('profile_picture')
    if request.data.get('street'):
        data_context['street'] = request.data.get('street')
    if request.data.get('street2'):
        data_context['street2'] = request.data.get('street2')
    if request.data.get('city'):
        data_context['city'] = request.data.get('city')
    if request.data.get('country'):
        data_context['country'] = request.data.get('country')
    if request.data.get('state'):
        data_context['state'] = request.data.get('state')
    if request.data.get('post_zip_code'):
        data_context['post_zip_code'] = request.data.get('post_zip_code')
    if request.data.get('show_email_address'):
        data_context['show_email_address'] = request.data.get('show_email_address')

    serializer = StoreSerilaizer(data=data_context)
    if serializer.is_valid():

        if request.data.get('store_name'):
            store.store_name = request.data.get('store_name')

        if request.data.get('store_products_per_page'):
            store.store_products_per_page = request.data.get('store_products_per_page')

        if request.data.get('store_banner'):
            store.store_banner = request.data.get('store_banner')

        if request.data.get('profile_picture'):
            store.profile_picture = request.data.get('profile_picture')

        if request.data.get('street'):
            store.street = request.data.get('street')

        if request.data.get('street2'):
            store.street2 = request.data.get('street2')

        if request.data.get('city'):
            store.city = request.data.get('city')

        if request.data.get('country'):
            store.country = request.data.get('country')
            
        if request.data.get('state'):
            store.state = request.data.get('state')

        if request.data.get('post_zip_code'):
            store.post_zip_code = request.data.get('post_zip_code')

        # if request.data.get('show_email_address'):
        #     store.street = request.data.get('street')
        store.save()
        return Response({'Message':'Store details updated successfully'})
    else:
        data = serializer.errors
        return Response(data)