from django import template
from django.db.models import Count

from shop.models import *

register = template.Library()


@register.inclusion_tag('products/mytegs/list_categories.html')
def show_categories(sort=None):
    cats = Category.objects.annotate(Count('product'))
    return {'cats': cats}
