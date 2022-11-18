from django.shortcuts import render, HttpResponseRedirect
from .models import Basket
from products.models import Product


def orders(request):
    context = {'title': 'Be Beloved - оформление заказа',
               'baskets': Basket.objects.all()}
    return render(request, 'baskets/orders.html', context)


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
