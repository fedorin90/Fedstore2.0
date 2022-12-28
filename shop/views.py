
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from cart.forms import CartAddProductForm
from .models import *
from .utils import DataMixin


class ShopHome(DataMixin, ListView):
    model = Product
    template_name = 'products/all_products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Home')
        return context | c_def


class ShopCategory(DataMixin, ListView):
    model = Product
    template_name = 'products/category.html'
    context_object_name = 'products'
    slug_url_kwarg = 'category_slug'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['products'][0].category))
        return context | c_def


class ShopDetail(DataMixin, DetailView, FormMixin):
    model = Product
    template_name = 'products/detail.html'
    form_class = CartAddProductForm

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['product'].name) + ' - details')
        return context | c_def



