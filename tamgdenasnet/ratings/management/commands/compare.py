from django.core.management import BaseCommand
import openpyxl, os

from ratings.models import Country, Cost, Democracy, Peace, Quality, Climate

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('hello')
        countries = Country.objects.all()
        print(countries.count())
        max_cost = countries.filter(cost__year=2023).count()
        for country in countries:
            try:
                peace = country.peace.get(year=2022).rating
                demo = country.democracy.get(year=2022).rating
                cost = max_cost - country.cost.get(year=2023).rating
                if cost > 80:
                    continue
                # climate = country.climate.get(year=2023).rating
                climate = 0
                # cost = country.cost.get(year=2023).rating
                print(country.name, peace, demo, cost, climate)
                # country.o_rating = i
                country.o_score = peace + demo + cost + climate
                # country.save()
                print(country.o_score)

            except Exception as error:
                print(country.name, error)
                continue
        countries = list(countries)
        countries = filter(lambda x: hasattr(x, 'o_score'), countries)
        # print(countries)
        countries = sorted(countries, key=lambda country: country.o_score)
        i = 1
        for country in countries: 
            try:
                country.o_rating = i
                print(country.o_rating, country.name, country.o_score)
                i += 1
            except Exception as error:
                print(country.name, error)
                continue
