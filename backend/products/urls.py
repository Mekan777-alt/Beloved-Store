from django.urls import path
from products.views import shop, details

app_name = 'products_app'

urlpatterns = [
    path('', shop, name='shop'),
    path('details/<int:product_id>/', details, name='details'),
]