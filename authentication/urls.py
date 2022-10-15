
from django.contrib import admin
from django.urls import path, include

from authentication import views
from authentication.views import LoginUser, RegisterUser

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),

]
