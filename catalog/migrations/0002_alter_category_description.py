# Generated by Django 5.0.6 on 2024-06-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Описание'),
        ),
    ]