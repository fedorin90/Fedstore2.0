
from django.shortcuts import render, redirect, get_object_or_404


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')





