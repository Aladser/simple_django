from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Категории
        category_list = [
            {'name': 'бытовая химия'},
            {'name': 'автомобили'},
            {'name': 'продукты'},
        ]
        category_create_list = [Category(**ctg) for ctg in category_list]
        Category.objects.bulk_create(category_create_list)

        category_list = {}
        for ctg in Category.objects.all():
            category_list[ctg.name] = ctg.pk

        product_list = [
            {'name': 'хлеб', 'category_id': category_list['продукты']},
            {'name': 'шампунь', 'category_id': category_list['бытовая химия']},
            {'name': 'Жигули', 'category_id': category_list['автомобили']},
        ]
        product_create_list = [Product(**prd) for prd in product_list]
        Product.objects.bulk_create(product_create_list)


