from django.shortcuts import render, HttpResponseRedirect
from .models import Basket
from products.models import Product


def orders(request):
    total_sum = 0
    total_quantity = 0
    baskets = Basket.objects.all()
    for basket in baskets:
        total_quantity += basket.quantity
        total_sum += basket.sum()
    context = {'title': 'Be Beloved - оформление заказа',
               'baskets': baskets,
               'total_quantity': total_quantity,
               'total_sum': total_sum}
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
