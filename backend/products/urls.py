from django.urls import path
from products.views import products

app_name = 'products_app'

urlpatterns = [
    path('', products, name='products'),
]