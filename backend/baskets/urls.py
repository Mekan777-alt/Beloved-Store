from django.urls import path
from baskets.views import basket, orders

app_name = 'basket_app'

urlpatterns = [
    path('basket/', basket, name='basket'),
    path('orders/', orders, name='orders'),
]