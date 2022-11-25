from django.urls import path
from baskets.views import cart, basket_add, checkout

app_name = 'basket_app'

urlpatterns = [
    path('', cart, name='cart'),
    path('cart', checkout, name='checkout'),
    path('basket_add<int:product_id>/', basket_add, name='basket_add'),
]
