from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.template.loader import render_to_string
from .forms import OrdersForms
from .models import Basket, Orders
from products.models import Product
from django.contrib import messages
from django.urls import reverse


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
    baskets = Basket.objects.all()
    if request.method == 'POST':
        forms = OrdersForms(request.POST)
        if forms.is_valid():
            try:
                forms.save()
                messages.success(request, 'Заказ оформлен!\n'
                                          'Менеджер созвонится с вами')
                # return redirect('index')
            except:
                forms.add_error(None, 'Ошибка добавление')
    else:
        forms = OrdersForms()
    context = {'title': 'Be Beloved - оформление заказа',
               'baskets': baskets,
               'form': forms}
    return render(request, 'baskets/checkout.html', context)


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


def basket_remove(request):
    basket = Basket.objects.all()
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('baskets/cart.html', context)
        return JsonResponse({'result': result})
