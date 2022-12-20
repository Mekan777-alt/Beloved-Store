from django.urls import path
from products.views import shop, details
from baskets.views import basket_add

app_name = 'products_app'

urlpatterns = [
    path('', shop, name='shop'),
    path('details/<int:product_id>/', details, name='details'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
]