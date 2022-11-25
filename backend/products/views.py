from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {'title': 'Be Beloved',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all()}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'Be Beloved - продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               }
    return render(request, 'products/product.html', context)


def shop(request):
    context = {'title': 'Be Beloved - продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               }
    return render(request, 'products/shop.html')

