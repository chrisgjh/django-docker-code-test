from django.urls import path
from django.contrib import admin

from questionnaire import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/", views.index, name="index"),
    path("questionnaire", views.questionnaire, name="questionnaire"),
    path("results", views.results, name="results"),
    path("admin", admin.site.urls),
]
