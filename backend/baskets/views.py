from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('basket_app:cart')


def cart_remove(request):
    cart = Cart(request)
    cart.remove()
    return redirect('basket_app:cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'baskets/cart.html', {'cart': cart})
