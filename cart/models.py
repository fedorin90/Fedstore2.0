from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.models import Product


class CartCreate(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, verbose_name=_(u"User"), blank=True, null=True)
    session = models.CharField(_(u"Session"), blank=True, max_length=100)
    creation_date = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    modification_date = models.DateTimeField(_(u"Modification date"), auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(CartCreate, models.CASCADE, verbose_name=_(u"Cart"))
    product = models.ForeignKey(Product, models.CASCADE, verbose_name=_(u"Product"))
    amount = models.FloatField(_(u"Quantity"), blank=True, null=True)
    creation_date = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    modification_date = models.DateTimeField(_(u"Modification date"), auto_now=True)
