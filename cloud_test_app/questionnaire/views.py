from django.shortcuts import render
from .forms import MonthForm, DayOfWeekForm

def index(request):
    # TODO: make this a real number:
    num_answers = 0
    context = {
        "title": "Basic Questions!",
        "num_answers": num_answers,
    }
    return render(request, "questionnaire/index.html", context)


def questionnaire(request):
    monform = MonthForm(request.POST or None)
    if monform.is_valid():
        monform.save()
        monform = MonthForm()
    
    dayform = DayOfWeekForm(request.POST or None)
    if dayform.is_valid():
        dayform.save()
        dayform = DayOfWeekForm()
    
    context = {
        "monform": monform,
        "dayform": dayform,
    }
    return render(request, "questionnaire/questionnaire.html", context)

def results(request):
    return render(request, "questionnaire/results.html")