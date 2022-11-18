from django.db import models
from products.models import Product


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    def sum(self):
        return self.quantity * self.product.price

