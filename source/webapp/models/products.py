from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class CategoryChoice(TextChoices):
    FOOD = 'food', 'Еда'
    CLOTHING = 'clothing', 'Одежда'
    TECH = 'tech', 'Техника'
    DRINKS = 'drinks', 'Напитки'
    OTHER = 'other', 'Разное'


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    image = models.CharField(max_length=100, null=True, blank=True, verbose_name="Фото")
    category = models.CharField(max_length=20, null=False, blank=False, choices=CategoryChoice.choices,
                                default=CategoryChoice.OTHER, verbose_name="Категория")
    remains = models.PositiveIntegerField(null=False, verbose_name="Остаток")
    price = models.DecimalField(null=False, max_digits=7, decimal_places=2, verbose_name="Стоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_deleted = models.BooleanField(null=False, default=False, verbose_name="Удален")
    deleted_at = models.DateTimeField(null=True, default=None, verbose_name="Дата и время удаления")

    def __str__(self):
        return f'{self.name} | {self.category} | {self.remains} | {self.price}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()
