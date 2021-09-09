from django.shortcuts import render, redirect
from .forms import MonthForm, DayOfWeekForm
from .models import FavMonth

def index(request):
    # TODO: make this a real number:
    num_answers = FavMonth.objects.count()
    context = {
        "title": "Basic Questions!",
        "num_answers": num_answers,
    }
    return render(request, "questionnaire/index.html", context)


def questionnaire(request):
    print(request.POST)
    monform = MonthForm(request.POST or None)
    dayform = DayOfWeekForm(request.POST or None)
    if monform.is_valid() and dayform.is_valid():
        monform.save()
        dayform.save()
        monform = MonthForm()
        dayform = DayOfWeekForm()
        return redirect('../')
    
    context = {
        "monform": monform,
        "dayform": dayform,
    }
    return render(request, "questionnaire/questionnaire.html", context)

def results(request):
    return render(request, "questionnaire/results.html")