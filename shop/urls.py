from django.urls import path, include
from shop.views import *

urlpatterns = [
    path('', ShopHome.as_view(), name='all_products'),
    path('item/<slug:slug>/', ShopDetail.as_view(), name='product_detail'),
    path('search/<slug:category_slug>/', ShopCategory.as_view(), name='category_list'),
]


