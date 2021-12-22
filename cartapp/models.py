from django.db import models
from django.conf import settings
from mainapp.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart",
                             verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveIntegerField(verbose_name="Колличество", default=0)
    add_datetime = models.DateTimeField(verbose_name="Время", auto_now_add=True)
