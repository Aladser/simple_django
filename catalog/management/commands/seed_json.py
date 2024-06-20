import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_data(filename='data.json'):
        """получает данные из JSON файла"""
        data = {'categories': [], 'products': []}

        with open(filename, 'r', encoding='utf8') as file:
            file_data = json.load(file)

        for elem in file_data:
            if elem['model'] == 'catalog.category':
                data['categories'].append(elem['fields']['name'])
            else:
                data['products'].append({'name': elem['fields']['name'], 'category': elem['fields']['category']})
        return data

    def handle(self, *args, **kwargs):
        json_data = self.json_read_data()

        [print(el) for el in json_data['categories']]
        [print(el) for el in json_data['products']]