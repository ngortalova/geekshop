from django.db import models
from django.db.models.fields import DecimalField, IntegerField
from django.db.models.fields.related import ForeignKey
# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя",
                            max_length=64,
                            unique=True)
    description = models.TextField(verbose_name="описание",
                                   blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="имя",
                            max_length=128,
                            unique=True)
    description = models.TextField(verbose_name="описание",
                                   blank=True)
    category = ForeignKey(ProductCategory, on_delete=models.SET_NULL,
                          null=True)
    short_description = models.CharField(verbose_name="короткое описание",
                                         max_length=64,
                                         blank=True)
    price = DecimalField(verbose_name="цена",
                         max_digits=8,
                         decimal_places=2,
                         default=0)
    price_with_discount = DecimalField(verbose_name="цена со скидкой",
                                       max_digits=8,
                                       decimal_places=2,
                                       default=0)
    quantity = IntegerField(verbose_name="кол-во на складе",
                            default=0)
    image = models.ImageField(upload_to="products_images",
                              blank=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"
