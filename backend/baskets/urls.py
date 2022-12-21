from django.urls import path
from baskets.views import cart, basket_add, basket_remove, checkout, basket_edit

app_name = 'basket_app'

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
    path('basket-remove/', basket_remove, name='basket_remove')
]
