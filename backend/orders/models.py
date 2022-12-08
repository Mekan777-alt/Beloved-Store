from django.db import models


class Orders(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.TextField()
    address = models.TextField()
    index = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.name} - {self.lastname}'
