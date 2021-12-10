import random

from django.core.management import BaseCommand

from faker import Faker

from students.models import Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=10)

    def handle(self, count, **options):
        fake = Faker()

        students = [
            Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(19, 39),
            )
            for _ in range(count)
        ]

        Student.objects.bulk_create(students)

        print(f'{count} students have been generated and saved to DB')
