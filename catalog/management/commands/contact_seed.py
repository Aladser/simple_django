from django.core.management import BaseCommand

from catalog.models import Contact


class Command(BaseCommand):
    contacts_list = [
        {'pk': 1, 'inn': 1111111, 'country': 'Россия', 'address': 'г.Москва'},
        {'pk': 2, 'inn': 2222222, 'country': 'Россия', 'address': 'г.Казань'},
        {'pk': 3, 'inn': 3333333, 'country': 'Беларусь', 'address': 'г.Львов'},
    ]

    def handle(self, *args, **kwargs):
        Contact.objects.all().delete()
        product_create_list = [Contact(**prd) for prd in self.contacts_list]
        Contact.objects.bulk_create(product_create_list)
