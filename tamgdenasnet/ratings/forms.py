# forms.py
from django import forms
from .models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        # На основе какой модели создаётся класс формы
        model = Rating
        # Укажем, какие поля будут в форме
        fields = ('name',)
