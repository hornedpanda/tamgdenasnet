from django.contrib import admin

# Register your models here.

from .models import Country, Rating, Country_Rating


class CountryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name',)
    ordering = ['pk', 'name']
    list_editable = ('name', 'slug')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'decreasing') 
    search_fields = ('name',) 
    ordering = ['pk']
    list_editable = ('name', 'slug', 'decreasing')


class Country_RatingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'country', 'rating', 'value', 'year') 
    search_fields = ('country__name', 'rating__name') 
    ordering = ['pk']
    # list_editable = ('country', 'rating')


admin.site.register(Country, CountryAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Country_Rating, Country_RatingAdmin)
