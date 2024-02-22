from django.core.management import BaseCommand
import openpyxl, os

from ratings.models import Country, Climate

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('hello')
        countries = Country.objects.all()
        print(countries.count())
        countries = countries.filter(cost__year=2023).count()
