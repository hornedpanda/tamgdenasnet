from django.db import models
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rating(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    decreasing = models.BooleanField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Country_Rating(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='country_rating',
        )
    rating = models.ForeignKey(
        Rating,
        on_delete=models.CASCADE,
        related_name='country_rating',
        )
    # place = models.PositiveSmallIntegerField()
    value = models.FloatField()
    year = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['country', 'rating', 'year'],
                                    name='unique_country_rating_year'),
        ]

    def __str__(self):
        return (f"{self.country.name} имеет {self.value}"
                f" баллов в рейтинге {self.rating.name} в {self.year} году")
    
    def get_place(self):
        records = Country_Rating.objects.filter(
            rating=self.rating).filter(year=self.year).order_by(
            '-value' if self.rating.decreasing == 0 else 'value')
        k = 1
        for record in records:
            if record.country == self.country:
                countries_count = records.count()
                koef = 100 - round(k/countries_count*100)
                # return (f"{k} место из {records.count()} ({koef}%)")
                place = {
                    'place': k,
                    'overall': records.count(),
                    'koef': koef
                }
                return place
            else:
                k += 1
        # place = records.get(country=self.country).record.place
        return (None)


