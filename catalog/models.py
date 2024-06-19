from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    ava = models.ImageField(upload_to='students/', verbose_name='Аватар', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('surname',)