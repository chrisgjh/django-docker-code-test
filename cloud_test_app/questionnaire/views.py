from django.shortcuts import render, redirect
from .forms import MonthForm, DayOfWeekForm
from .models import FavMonth, FavDayOfWeek

def index(request):
    # TODO: make this a real number:
    num_answers = FavMonth.objects.count()
    context = {
        "title": "Basic Questions!",
        "num_answers": num_answers,
    }
    return render(request, "questionnaire/index.html", context)


def questionnaire(request):
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
    favmon = FavMonth.objects.all()
    favday = FavDayOfWeek.objects.all()

    #--------------------------- Month Section --------------------------
    unique_mon = dict()
    for mon in favmon:
        if mon.month in unique_mon:
            unique_mon[mon.month] += 1
        elif mon.month not in unique_mon:
            unique_mon[mon.month] = 1

    sum_mon = sum(unique_mon.values())

    percentage_mon = list()
    for i in unique_mon.values():
        percentage_mon.append("{:.1f}".format(i/sum_mon*100))
    
    counter_mon = 0
    mon_info = list()
    for i,j in unique_mon.items():
        mon_info.append((i, j, percentage_mon[counter_mon]))
        counter_mon += 1

    #--------------------------- Day Section ----------------------------
    unique_day = dict()
    for day in favday:
        if day.dayofweek in unique_day:
            unique_day[day.dayofweek] += 1
        elif day.dayofweek not in unique_day:
            unique_day[day.dayofweek] = 1

    sum_day = sum(unique_day.values())

    percentage_day = list()
    for j in unique_day.values():
        percentage_day.append("{:.1f}".format(j/sum_day*100))

    counter_day = 0
    day_info = list()
    for k,l in unique_day.items():
        day_info.append((k, l, percentage_day[counter_day]))
        counter_day += 1
    
    #-------------------- Fav Day to Month Section ------------------------
    day_to_mon = dict()
    for z in unique_mon.keys():
        day_to_mon[z] = dict()
    
    for m in range(len(favmon)):
        mon_key = favmon[m].month
        day_key = favday[m].dayofweek
        if day_key in day_to_mon[mon_key].keys():
            day_to_mon[mon_key][day_key] += 1
        elif day_key not in day_to_mon[mon_key].keys():
            day_to_mon[mon_key][day_key] = 1

    results = []
    for n in day_to_mon.keys():
        day_dict = day_to_mon[n]
        results.append([n, max(day_dict, key=day_dict.get)])

    context = {
        "favmon": favmon,
        "favday": favday,
        "mon_info": mon_info,
        "day_info": day_info,
        "results": results,
    }
    return render(request, "questionnaire/results.html", context)