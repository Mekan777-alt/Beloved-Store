from django.urls import path
from orders.views import checkout

app_name = 'orders_app'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
]
