from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from baskets.models import Basket


def index(request):
    context = {'title': 'Be Beloved | Начало',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all()}
    return render(request, 'products/index.html', context)


# def details(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {'title': 'Be Beloved | Продукты',
#                'products': Product.objects.all(),
#                'category': ProductCategory.objects.all(),
#                'product': product,
#                }
#     return render(request, 'products/product-details.html', context)


def shop(request):
    context = {'title': 'Be Beloved | Продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               'baskets': Basket.objects.all()
               }
    return render(request, 'products/shop.html', context)


from baskets.forms import CartAddProductForm


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'title': 'Be Beloved | Продукты',
               'products': Product.objects.all(),
               'category': ProductCategory.objects.all(),
               'product': product,
               'cart_product_form': CartAddProductForm()
               }
    return render(request, 'products/product-details.html', context)
