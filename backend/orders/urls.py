from django.urls import path
from .views import order_create, checkout

app_name = 'order_app'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('create/', order_create, name='order_create')
]
