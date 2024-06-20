from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Категории
        category_list = [
            {'pk': 1, 'name': 'автомобили'},
            {'pk': 2, 'name': 'бытовая химия'},
            {'pk': 3, 'name': 'продукты'},
        ]
        category_create_list = [Category(**ctg) for ctg in category_list]
        Category.objects.bulk_create(category_create_list)

        category_list = {}
        for ctg in Category.objects.all():
            category_list[ctg.name] = ctg.pk

        product_list = [
            {'pk': 1, 'name': 'Жигули', 'category_id': category_list['автомобили']},
            {'pk': 2, 'name': 'Хлеб', 'category_id': category_list['продукты']},
            {'pk': 3, 'name': 'Шампунь', 'category_id': category_list['бытовая химия']},
        ]
        product_create_list = [Product(**prd) for prd in product_list]
        Product.objects.bulk_create(product_create_list)


