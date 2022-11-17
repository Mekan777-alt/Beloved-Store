from django.urls import path
from baskets.views import basket, orders, basket_add

app_name = 'basket_app'

urlpatterns = [
    path('', basket, name='basket'),
    path('', orders, name='orders'),
    path('basket_add<int:product_id>/', basket_add, name='basket_add')
]