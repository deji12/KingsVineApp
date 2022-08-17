from django.shortcuts import render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import uuid
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import OrderModel
from products.models import Product
from kvapp.models import User
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import stripe

stripe.api_key = "sk_test_51LXlZsBz09LwdcjaxIJTEKWIF0RaVOe0HyAqJ2mE3N5ysEWj7ZE1mGuCfvDmzibpBBVIxhPQLZR8diWVpHOfhliK00iHGNtYEQ"

# @api_view(['POST', 'GET'])
@csrf_exempt
def Home(request):
    if request.method == 'POST': 
        #get incoming data
        product_name = request.POST.get('product_name')
        vendor = request.POST.get('vendor')
        price = request.POST.get('price')
        customer = request.POST.get('customer')
        quantity = request.POST.get('quantity')
        code = 'USD'
        print(product_name)

        splitted_product_name = product_name.split(",")
        for i in splitted_product_name:
            pass

        # create new order model
        get_vendor = User.objects.get(email=vendor)
        get_product = Product.objects.get(name=product_name, vendor=get_vendor)

        create_new_order = OrderModel.objects.create(
            product_vendor = get_vendor,
            product_name = get_product,
            product_price = price,
            customer = User.objects.get(username=customer),
        )
        create_new_order.quantity += int(quantity)
        #save order model
        create_new_order.save()

        #details for paypal payment
        host = request.get_host()
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': price,
            'item_name': product_name,
            # 'invoice': str(uuid.uuid4()),
            'invoice': str(create_new_order.id),
            'currency_code': code,
            'quantity': quantity,
            'notify_url': f'http://{host}{reverse("paypal-ipn")}',
            'return_url': f'http://{host}{reverse("paypal-return")}',
            'cancel_return': f'http://{host}{reverse("paypal-cancel")}',
        }
        # paypal form
        form  = PayPalPaymentsForm(initial=paypal_dict)
        context = {
            'form': form
            }
    return render(request, 'send.html')
    

@api_view(['GET'])
def paypal_return(request):
    # return HttpResponse('You have successfully made a payment')
    email_templat_name = 'email_template.html'
    user = User.objects.get(email=request.user)
    c = {
        'username': user.username
    }
    emaill = render_to_string(email_templat_name, c)     

    email_mess = EmailMessage (
        'KingsVine: Product Purchase',
        emaill,
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    email_mess.fail_silently = True
    email_mess.content_subtype = 'html'
    email_mess.send()

    messages.success(request, 'You have successfully made a payment')
    return redirect('home')

@api_view(['GET'])
def paypal_cancel(request):
    # return HttpResponse('You  order has been cancelled')
    messages.error(request, 'You  order has been cancelled')
    return redirect('home')




