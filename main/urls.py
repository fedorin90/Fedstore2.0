
from django.contrib import admin
from django.urls import path, include

from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('single/', views.single, name='single'),
    path('auth/', include('authentication.urls')),
]
