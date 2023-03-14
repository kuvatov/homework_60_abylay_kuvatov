from django.db import models

from webapp.models import Product


class Cart(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT,
        verbose_name='Продукт'
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        default=1
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время добавления"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    def __str__(self):
        return f'{self.product} | {self.quantity}'
