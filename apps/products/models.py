from django.db import models

from apps.categorits.models import Categorits

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(
        Categorits, on_delete = models.CASCADE,
        related_name = "category_products",
        verbose_name = "Категория",
        blank = True, null = True,
    )
    title = models.CharField(
        max_length = 255, 
        verbose_name = "Название товара"
    )
    description = models.TextField(
        verbose_name = "Описание товара"
    )
    price = models.PositiveBigIntegerField(
        verbose_name = "Цена товара"
    )
    image = models.ImageField(
        upload_to='product_image/',
        verbose_name="Фотография товара"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"