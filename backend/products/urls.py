from django.urls import path
from products.views import products, shop

app_name = 'products_app'

urlpatterns = [
    path('', shop, name='shop'),
    path('', products, name='products'),
]