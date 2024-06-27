from django.core.management import BaseCommand

from catalog.models import Category, Product, Contact


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
    # контакты
    contacts_list = [
        {'pk': 1, 'name': 'Помидоркин', 'number': 10000001, 'address': 'Москва'},
        {'pk': 2, 'name': 'Птичкин', 'number': 10000002, 'address': 'Питер'},
        {'pk': 3, 'name': 'Светлов', 'number': 10000003, 'address': 'Тверь'},
        {'pk': 4, 'name': 'Губкина', 'number': 10000004, 'address': 'Новосибирск'},
        {'pk': 5, 'name': 'Аксенова', 'number': 10000005, 'address': 'Иркутск'},
    ]

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contact.objects.all().delete()

        category_create_list = [Category(**ctg) for ctg in self.category_list]
        Category.objects.bulk_create(category_create_list)

        product_create_list = [Product(**prd) for prd in self.product_list]
        Product.objects.bulk_create(product_create_list)

        product_create_list = [Contact(**prd) for prd in self.contacts_list]
        Contact.objects.bulk_create(product_create_list)