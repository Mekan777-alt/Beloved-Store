from django.conf.urls import url
from django.urls import path
from products.views import shop, product_detail

app_name = 'products_app'

urlpatterns = [
    path('', shop, name='shop'),
    path('details/<int:product_id>/', product_detail, name='details'),
    # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', details, name='detail'),
]