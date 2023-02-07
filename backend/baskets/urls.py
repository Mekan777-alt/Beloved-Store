from django.conf.urls import url
from . import views

app_name = 'basket_app'


urlpatterns = [
    url(r'^$', views.cart_detail, name='cart'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='basket_add'),
    url(r'^remove/', views.cart_remove, name='basket_remove'),
]
