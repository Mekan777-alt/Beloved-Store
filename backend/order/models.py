from django.db import models
from baskets.models import Basket


class Orders(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.TextField()
    address = models.TextField()
    city = models.TextField()
    index = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.name} - {self.lastname}'


class OrderItem(models.Model):
    order_name = models.CharField(max_length=250)
    order_pn = models.CharField(max_length=20)
    order_eaddress = models.TextField(default=0)
    order_address = models.TextField()
    product_name = models.CharField(max_length=400)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.order_name} - {self.product_name}'

