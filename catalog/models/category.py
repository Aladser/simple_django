from django.db import models


class Category(models.Model):
    """Категория"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.CharField(max_length=256, verbose_name='Описание', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)
