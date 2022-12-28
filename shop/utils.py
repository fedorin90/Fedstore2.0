from cart.forms import CartAddProductForm
from shop.models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['cart_product_form'] = CartAddProductForm()
        cats = Category.objects.all()
        products = Product.objects.all()
        context['products'] = products
        context['cats'] = cats
        return context



