
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from cart.forms import CartAddProductForm
from .models import *


class ShopHome(ListView):
    model = Product
    template_name = 'products/all_products.html'
    context_object_name = 'products'
    extra_context = {'title': 'Home'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShopCategory(ListView):
    model = Product
    template_name = 'products/category.html'
    context_object_name = 'products'
    slug_url_kwarg = 'category_slug'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category - ' + str(context['products'][0].category)
        return context


class ShopDetail(DetailView, FormMixin):
    model = Product
    template_name = 'products/detail.html'
    form_class = CartAddProductForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context



