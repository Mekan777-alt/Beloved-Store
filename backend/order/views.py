from django.shortcuts import render
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
    basket = Basket.objects.all()
    product_name = basket[0]
    if request.method == 'POST':
        form = OrdersForms(request.POST)
        if form.is_valid():
            form.save()
            orders = Orders.objects.all()
            print(orders)
            # OrderItem.objects.create(order_name=orders[0],
            #                          order_pn=orders[6],
            #                          order_eaddress=order_email,
            #                          order_address=order_address,
            #                          product_name=product_name,
            #                          quantity=1)
            # basket.delete()
            return render(request, 'orders/created.html')
    else:
        form = OrdersForms()
    return render(request, 'orders/checkout.html', {'basket': basket, 'form': form})
