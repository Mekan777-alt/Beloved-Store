from django.shortcuts import render
from baskets.cart import Cart
from baskets.models import Basket
from order.forms import OrdersForms
from .models import Orders, OrderItem


def checkout(request):
    forms = OrdersForms()
    baskets = Basket.objects.all()
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)
    context = {'title': 'Be Beloved - оформление заказа',
               'form': forms,
               'total_quantity': total_quantity,
               'total_sum': total_sum
               }
    return render(request, 'orders/checkout.html', context)


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrdersForms(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrdersForms
    return render(request, 'orders/checkout.html',
                  {'cart': cart, 'form': form})
