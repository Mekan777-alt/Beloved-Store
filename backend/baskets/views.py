from django.shortcuts import render, HttpResponseRedirect
from .models import Basket
from products.models import Product


def basket(request):
    context = {'title': 'By Beloved - корзина',
               'baskets': Basket.objects.all()}
    return render(request, 'baskets/baskets.html', context)


def orders(request):
    context = {'title': 'By Beloved - оформление заказа'}
    return render(request, 'baskets/checkout_order.html', context)


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
