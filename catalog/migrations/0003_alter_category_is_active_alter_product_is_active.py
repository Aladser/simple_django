# Generated by Django 5.0.6 on 2024-06-20 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
    ]