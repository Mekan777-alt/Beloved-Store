from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {'title': 'Be Beloved'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'Be Beloved - продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               }
    return render(request, 'products/products.html', context)
