from django.contrib import admin

from .models import FavMonth
from .models import FavDayOfWeek

admin.site.register(FavMonth)
admin.site.register(FavDayOfWeek)