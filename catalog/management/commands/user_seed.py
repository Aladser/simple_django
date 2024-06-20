from django.core.management import BaseCommand

from catalog.models import Student


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        student_list = [
            {'name':'Иван', 'surname':'Молодцов'},
            {'name':'Саша', 'surname': 'Городской'},
            {'name':'Ваня', 'surname': 'Ветров'},
            {'name':'Катя', 'surname': 'Кузнецова'},
            {'name':'Юля', 'surname': 'Клюева'}
        ]

        # одиночное создание строк таблицы
        #for student in student_list:
        #    Student.objects.create(**student)

        # массовое создание
        student_obj_list = []
        for student in student_list:
            student_obj_list.append(Student(**student))
        Student.objects.bulk_create(student_obj_list)
