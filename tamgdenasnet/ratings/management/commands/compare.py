from django.core.management import BaseCommand
import openpyxl, os

from ratings.models import Country, Rating, Country_Rating

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('hello')
        countries = Country.objects.all()
        print(countries.count())
        print(countries)
        for country in countries:
            try:
                peace = country.country_rating.get(
                    year=2022,
                    rating_id=1
                    ).value
                print(country, peace)
            except Exception as error:
                print(country.name, error)
                continue
