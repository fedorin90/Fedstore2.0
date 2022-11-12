from django.urls import path, include

from shop import views


urlpatterns = [

    # path('product/', views.product, name='product'),
    # path('single/<slug:slug>/', views.single, name='single'),
    # path('product/<slug:slug>/', views.product, name='product_by_category'),

    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),

]


