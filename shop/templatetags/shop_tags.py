from django import template
from django.db.models import Count
import re
import math
from shop.models import *

register = template.Library()


@register.inclusion_tag('products/mytegs/list_categories.html')
def show_categories(sort=None):
    cats = Category.objects.annotate(Count('product'))
    return {'cats': cats}


@register.filter
def set_page(uri, number):
    """Sets `page` property to uri string"""

    if '?page=' in uri or '&page=' in uri:
        uri = re.sub(r'page=[\d]+', f'page={number}', uri)
    elif re.search(r'/?[\w]+=', uri):
        uri = f'{uri}&page={number}'
    else:
        uri = f'?page={number}'

    return uri


@register.filter
def remove_page(uri):
    """Removes `page` property from uri string"""

    if '?page=' in uri or '&page=' in uri:
        uri = re.sub(r'[?&]page=[\d]+', '', uri)
    if re.search('/&', uri):
        uri = re.sub('/&', '/?', uri)

    return uri


@register.filter(name='round')
def round_to(number, to=100):
    return int(math.ceil(number / to)) * to