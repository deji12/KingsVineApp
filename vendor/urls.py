from django.urls import path
from . import views

urlpatterns = [
    path('update-store/', views.UpdateStore),
]