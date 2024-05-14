﻿from django.contrib.auth.views import (LoginView, LogoutView, 
    PasswordResetView, PasswordChangeView, PasswordChangeDoneView)
# from django.contrib.auth import views
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
      'logout/',
      # Прямо в описании обработчика укажем шаблон, 
      # который должен применяться для отображения возвращаемой страницы.
      # Да, во view-классах так можно! Как их не полюбить.
      LogoutView.as_view(template_name='users/logged_out.html'),
      name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password_change/', 
         PasswordChangeView.as_view(
            template_name='users/password_change.html'),
         name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'
         ),
         name='password_change_done'),
    path('password_reset/',
         PasswordResetView.as_view(),
         name='password_reset_form'
         ),
    
] 