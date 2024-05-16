from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Max

# Create your views here.

from django.http import HttpResponse
from .models import Country, Rating, Country_Rating


# Главная
def index(request):
    template = 'ratings/index.html'
    title = 'Список стран'
    year = 2023
    rating_name = 'Global Peace Index GPI'
    rating = Rating.objects.get(name=rating_name)
    # print(rating)
    # if Country_Rating.objects.get(name='rating_name')
    # countries = Country.objects.all()[:100]
    # if rating.decreasing == 0:
    #     country_rating = Country_Rating.objects.filter(
    #             rating=rating).filter(year=year).order_by('-value')
    # else:
    #     country_rating = Country_Rating.objects.filter(
    #             rating=rating).filter(year=year).order_by('value')
    country_rating = Country_Rating.objects.filter(
        rating=rating).filter(year=year).order_by(
        '-value' if rating.decreasing == 0 else 'value')
    paginator = Paginator(country_rating, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        # 'text': 'Тут табличка',
        'page_obj': page_obj,
        'start_index': page_obj.start_index(),
        'year': year
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница рейтинга
def rating_detail(request, **kwargs):
    template = 'ratings/rating_detail.html'
    rating = get_object_or_404(Rating, slug=kwargs['slug'])
    year = kwargs.setdefault('year',
        Country_Rating.objects.aggregate(Max('year'))['year__max']
        )
    country_rating = Country_Rating.objects.filter(
        rating=rating).filter(year=year).order_by(
        '-value' if rating.decreasing == 0 else 'value')
    paginator = Paginator(country_rating, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'rating': rating,
        'page_obj': page_obj,
        'start_index': page_obj.start_index(),
        'year': year
    }
    return render(request, template, context) 


# Страница страны
def country_detail(request, **kwargs):
    template = 'ratings/country_detail.html'
    country = get_object_or_404(Country, slug=kwargs['slug'])
    # if kwargs['year']:
    year = kwargs.setdefault('year',
        Country_Rating.objects.aggregate(Max('year'))['year__max']
        )
    # else:
    # year = Country_Rating.objects.aggregate(Max('year'))['year__max']
    # year = year['year__max']
    country_ratings = Country_Rating.objects.filter(
        country=country).filter(year=year)
    for country_rating in country_ratings:
        # print(country_rating.get_place())
        country_rating.place = country_rating.get_place()
        country_rating.save()
    context = {
        'country': country,
        'country_ratings': country_ratings,
        'year': year
    }
    return render(request, template, context)