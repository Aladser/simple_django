from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Категории
        category_list = [
            {'name':'бытовая химия'},
            {'name': 'автомобили'},
            {'name': 'продукты'},
        ]
        category_create_list = [Category(**ctg) for ctg in category_list]
        Category.objects.bulk_create(category_create_list)

        category_list = []
        for ctg in Category.objects.all():
            category_list.append({'id':ctg.pk, 'name':ctg.name})

        print(*category_list)