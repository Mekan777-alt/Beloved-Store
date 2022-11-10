from django.shortcuts import render


def index(request):
    context = {'title': 'By Beloved'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'By Beloved - продукты'}
    return render(request, 'products/products.html', context)
