from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product, ProductCategory
from baskets.models import Basket


def index(request):
    context = {'title': 'Be Beloved | Начало',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all()}
    return render(request, 'products/index.html', context)


def details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'title': 'Be Beloved | Продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               'product': product,
               }
    return render(request, 'products/product-details.html', context)


def shop(request):
    context = {'title': 'Be Beloved | Продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               'baskets': Basket.objects.all()
               }
    return render(request, 'products/shop.html', context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(product=product)

    if not baskets:
        Basket.objects.create(product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

