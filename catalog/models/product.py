from django.db import models

from catalog.models.category import Category

NULLABLE = {
    'null': True,
    'blank': True
}


class Product(models.Model):
    """Товар"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.CharField(max_length=256, verbose_name='Описание', **NULLABLE)
    ava = models.ImageField(upload_to='img/products', verbose_name='Аватар', default=None, **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    manufactured_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата производства')
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='категория',
    )

    def __str__(self):
        return f"{self.name} ({self.category}{' '+str(self.price) if self.price else ''})"

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'товары'
        ordering = ('name', 'price', 'created_at', 'updated_at')

