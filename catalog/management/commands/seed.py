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
        {
            'pk': 1,
            'name': 'Жигули',
            'category_id': 1,
            'description': 'советский автомобиль',
            'price': 1000
        },
        {
            'pk': 2,
            'name': 'Мерседес',
            'category_id': 1,
            'description': 'немецкий автомобиль',
            'price': 2000
        },
        {
            'pk': 3,
            'name': 'Toyota',
            'category_id': 1,
            'description': 'японский автомобиль',
            'price': 300,
            'ava': 'toyota.jpeg'
        },
        {
            'pk': 4,
            'name': 'Шампунь',
            'category_id': 2,
            'description': 'для головы',
            'price': 300,
            'ava': 'shampoo.jpeg'
        },
        {
            'pk': 5,
            'name': 'Мыло',
            'category_id': 2,
            'description': 'для всего тела',
            'price': 100,
            'ava' : 'soap.jpeg'
        },
        {
            'pk': 6,
            'name': 'Крем',
            'category_id': 2,
            'description': 'для кожи',
            'price': 200,
            'ava': 'cream.jpeg'
        },
        {
            'pk': 7,
            'name': 'Хлеб',
            'category_id': 3,
            'description': 'всему голова',
            'price': 50,
            'ava': 'bread.png'
        },
    ]

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_create_list = [Category(**ctg) for ctg in self.category_list]
        Category.objects.bulk_create(category_create_list)

        product_create_list = [Product(**prd) for prd in self.product_list]
        Product.objects.bulk_create(product_create_list)
