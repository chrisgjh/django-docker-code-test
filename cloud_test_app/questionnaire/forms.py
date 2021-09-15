from django import forms
from .models import FavDate

class DateForm(forms.ModelForm):
    class Meta:
        model = FavDate
        fields = ['month', 'dayofweek']