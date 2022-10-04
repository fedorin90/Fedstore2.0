from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')


def single(request):
    return render(request, 'single.html')
