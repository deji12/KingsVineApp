from django.urls import path, include
from . import views

urlpatterns = [
    # path('signup/', views.CreateUsers, name='register'),
    # path('login/', views.LoginUsers, name='login'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted/', views.restricted),
    path('all-users/', views.all_users),
    path('update-user-password/', views.UpdateUserPassword),
    path('update-user-profile/', views.UpdateUserProfile),
]

# logout
# auth/token/logout

# login
# auth/token/login

# register
# auth/users

# reset password
# auth/users/set_password

