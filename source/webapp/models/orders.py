from django.db import models


class Order(models.Model):
    products = models.ManyToManyField(
        to='webapp.Product',
        verbose_name='Продукты'
    )
    user_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Имя пользователя'
    )
    phone = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Телефон'
    )
    address = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Адрес'
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
        return f'{self.user_name} | {self.phone} | {self.address}'
