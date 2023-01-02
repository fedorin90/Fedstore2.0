from cart.forms import CartAddProductForm
from shop.models import *


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        context['cart_product_form'] = CartAddProductForm()
        return context



