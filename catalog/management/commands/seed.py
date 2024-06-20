from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    # Категории
    category_list = [
        {'pk': 1, 'name': 'автомобили'},
        {'pk': 2, 'name': 'бытовая химия'},
        {'pk': 3, 'name': 'продукты'},
    ]
    # Товары
    product_list = [
        {'pk': 1, 'name': 'Жигули', 'category_id': 1},
        {'pk': 2, 'name': 'Хлеб', 'category_id': 3},
        {'pk': 3, 'name': 'Шампунь', 'category_id': 2},
    ]

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_create_list = [Category(**ctg) for ctg in self.category_list]
        Category.objects.bulk_create(category_create_list)

        product_create_list = [Product(**prd) for prd in self.product_list]
        Product.objects.bulk_create(product_create_list)


