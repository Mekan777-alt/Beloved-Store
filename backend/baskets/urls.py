from django.urls import path
from baskets.views import cart, basket_add, basket_remove

app_name = 'basket_app'

urlpatterns = [
    path('', cart, name='cart'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-remove/', basket_remove, name='basket_remove')
]
