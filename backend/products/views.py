from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {'title': 'By Beloved'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'By Beloved - продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               }
    return render(request, 'products/products.html', context)
