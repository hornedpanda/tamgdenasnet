from django.contrib.auth.views import LogoutView 
from django.urls import path
from . import views

app_name = 'ratings'

urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('rating/<slug:slug>/', views.rating_detail),
    path('country/<slug:slug>/', views.country_detail),
] 