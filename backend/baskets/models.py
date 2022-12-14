from django.db import models
from products.models import Product


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        baskets = Basket.objects.all()
        return sum(basket.quantity for basket in baskets)


class Orders(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    index = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.name} - {self.lastname}'
