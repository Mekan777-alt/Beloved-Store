from django.urls import path
from baskets.views import basket, orders

app_name = 'basket_app'

urlpatterns = [
    path('', basket, name='basket'),
    path('', orders, name='orders'),
]