from django.urls import path
from. import views

urlpatterns  = [
    path('add-shipping-address/', views.CreateShippingAddress, name='add-shipping-address'),
    path('add-billing-address/', views.CreateBillingAddress, name='add-billing-address'),
    path('user-shipping-address/', views.ViewUserShippingAddress, name='user-shipping-address'),
    path('user-billing-address/', views.ViewUserBillingAddress, name='user-billing-address'),
]