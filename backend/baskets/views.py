from django.shortcuts import render, HttpResponseRedirect
from .models import Basket
from products.models import Product


def cart(request):
    baskets = Basket.objects.all()
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)
    context = {'title': 'Be Beloved - оформление заказа',
               'baskets': baskets,
               'total_quantity': total_quantity,
               'total_sum': total_sum}
    return render(request, 'baskets/cart.html', context)


def checkout(request):
    return render(request, 'baskets/checkout.html')


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
