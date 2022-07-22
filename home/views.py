from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from kvapp.models import User
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response

@api_view(['GET'])
def HomePage(request):
    new_arrivals = Product.objects.all()[:8]
    get_collectors_product_pick = Product.objects.filter(collectors_pick=True)[:12]

    new_arrivals_serializer = ProductSerializer(data=new_arrivals, many=True)
    get_collectors_product_pick_serializer = ProductSerializer(data=get_collectors_product_pick, many=True)

    response = new_arrivals_serializer.data + get_collectors_product_pick_serializer.data

    return Response(response)

