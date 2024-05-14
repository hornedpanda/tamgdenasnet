from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200, unique=True)


class AbstractRatingModel(models.Model):
    rating = models.PositiveSmallIntegerField()
    value = models.FloatField()
    year = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.text


class Peace(models.Model):
    rating = models.PositiveSmallIntegerField()
    value = models.FloatField()
    # country = models.ForeignKey(
    #     Country,
    #     on_delete=models.CASCADE,
    #     related_name='peace',
    #     unique=True
    # )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='peace',
        # primary_key=True
        )
    year = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['country', 'year'],
                                    name='unique_country_year'),
        ]

    def __str__(self):
        return (f"{self.country.name} занимает {self.rating}"
                f" строчку в Global Peace Index в {self.year} году") 


class Democracy(models.Model):
    rating = models.PositiveSmallIntegerField(default=0)
    value = models.FloatField()
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='democracy',
        )
    year = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['country', 'year'],
                                    name='unique_country_year'),
        ]

    def __str__(self):
        return (f"{self.country.name} занимает {self.rating} строчку в"
                f" Democracy Index в {self.year} году")


class Cost(models.Model):
    rating = models.PositiveSmallIntegerField(default=0)
    cost_index = models.FloatField()
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='cost',
        )
    year = models.PositiveSmallIntegerField()
    rent_index = models.FloatField()
    cost_rent_index = models.FloatField()
    salary = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['country', 'year'],
                                    name='unique_country_year'),
        ]

    # def get_rating(self, field):
    #     return 

    def __str__(self):
        return (f"{self.country.name} занимает {self.rating} строчку в"
                f" Cost of Living Index в {self.year} году")


class Quality(models.Model):
    rating = models.PositiveSmallIntegerField(default=0)
    value = models.FloatField()
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='quality',
        )
    year = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['country', 'year'],
                                    name='unique_country_year'),
        ]

    def __str__(self):
        return (f"{self.country.name} занимает {self.rating} строчку в"
                f" Quality of Life Index в {self.year} году")


class Climate(AbstractRatingModel):

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='climate',
        # primary_key=True
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['country', 'year'],
                                    name='unique_country_year'),
        ]

    def __str__(self):
        return (f"{self.country.name} занимает {self.rating} строчку в"
                f" Quality of Life Index Climate в {self.year} году")