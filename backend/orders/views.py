from django.shortcuts import render
from baskets.models import Basket
from .forms import OrdersForms


def checkout(request):
    form = OrdersForms()
    baskets = Basket.objects.all()
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)
    context = {'title': 'Be Beloved - оформление заказа',
               'baskets': baskets,
               'total_quantity': total_quantity,
               'total_sum': total_sum,
               'form': form}
    return render(request, 'orders/checkout.html', context)
