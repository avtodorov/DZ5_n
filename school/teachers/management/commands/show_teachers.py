
from django.core.management import BaseCommand


from teachers.models import Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('choice', type=str, default='first_name', nargs='?', help='Choices are: first_name, '
                                                                                      'last_name, theme')
        parser.add_argument('name', type=str, nargs='?', help='Give a parameter name to search in data')

    def handle(self, choice, name, **options):

        if choice == 'last_name':
            data = Teacher.objects.filter(last_name=name)
        elif choice == 'theme':
            data = Teacher.objects.filter(theme=name)
        else:
            data = Teacher.objects.filter(first_name=name)

        print(f'Teachers with choice:{choice} with name:{name} : {data}')
