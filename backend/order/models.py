from django.db import models


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
    product_name = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.name} - {self.lastname}'
