from django.urls import path, include

from shop import views
from shop.views import *

urlpatterns = [
    path('', ShopHome.as_view(), name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', ShopCategory.as_view(), name='category_list'),
]


