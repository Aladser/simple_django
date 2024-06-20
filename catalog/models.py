from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.CharField(max_length=256, verbose_name='Описание',**NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.CharField(max_length=256, verbose_name='Описание', **NULLABLE)
    ava = models.ImageField(upload_to='img/products', verbose_name='Аватар', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='категория',
    )

    def __str__(self):
        return f"{self.name} [{self.price} {self.category}]"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'