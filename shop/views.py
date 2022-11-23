from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def all_products(request):
    cat = Category.objects.all()
    products = Product.products.all()
    context = {'products': products, 'title': 'Home', 'cat': cat}
    return render(request, 'products/all_products.html', context=context)


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    cat = Category.objects.all()
    context = {'category': category, 'products': products, 'cat': cat}
    return render(request, 'products/category.html', context=context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'products/detail.html', context=context)



