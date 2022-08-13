from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('paypal-return', views.paypal_return, name='paypal-return'),
    path('paypal-cancel', views.paypal_cancel, name='paypal-cancel'),
]