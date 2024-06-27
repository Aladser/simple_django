from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    number = models.CharField(max_length=11, verbose_name='Номер')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    def __str__(self):
        return f"{self.name}, {self.number}"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'контакты'
        ordering = ('name', 'number',)
