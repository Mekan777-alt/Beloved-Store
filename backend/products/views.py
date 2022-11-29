from django.shortcuts import render
from .models import Product, ProductCategory, ProductImage


def index(request):
    context = {'title': 'Be Beloved | Начало',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all()}
    return render(request, 'products/index.html', context)


def details(request, product_id):
    product = Product.objects.get(id=product_id)
    static_image = ProductImage.objects.get(id=product_id)
    context = {'title': 'Be Beloved | Продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               'product': product,
               'static_image': static_image
               }
    return render(request, 'products/product-details.html', context)


def shop(request):
    context = {'title': 'Be Beloved | Продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               }
    return render(request, 'products/shop.html', context)
