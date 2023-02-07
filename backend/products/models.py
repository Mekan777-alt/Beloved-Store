from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категория продуктов'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    image_static_shop = models.ImageField(upload_to='products_image', null=True, blank=True)
    image_static1 = models.ImageField(upload_to='products_image', null=True, blank=True)
    image_static2 = models.ImageField(upload_to='products_image', null=True, blank=True)
    image_static3 = models.ImageField(upload_to='products_image', null=True, blank=True)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'Продукт - {self.name}: Категория - {self.category}'
