from django import forms
from .models import FavMonth
from .models import FavDayOfWeek

class MonthForm(forms.ModelForm):
    class Meta:
        model = FavMonth
        fields = ['month']

class DayOfWeekForm(forms.ModelForm):
    class Meta:
        model = FavDayOfWeek
        fields = ['dayofweek']