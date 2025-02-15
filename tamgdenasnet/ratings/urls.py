﻿from django.contrib.auth.views import LogoutView 
from django.urls import path
from . import views

app_name = 'ratings'

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('rating/<slug:slug>/', views.rating_detail),
    path('rating/<slug:slug>/<int:year>/', views.rating_detail, name="rating"),
    path('country/<slug:slug>/', views.country_detail),
    path('country/<slug:slug>/<int:year>/',
         views.country_detail,
         name="country"
         ),
] 