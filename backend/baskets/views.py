from django.shortcuts import render
from .models import Basket


def basket(request):
    context = {'title': 'By Beloved - корзина',
               'basket': Basket.objects.all()}
    return render(request, 'baskets/baskets.html', context)


def orders(request):
    context = {'title': 'By Beloved - оформление заказа'}
    return render(request, 'baskets/checkout_order.html', context)