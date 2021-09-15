from django.shortcuts import render, redirect
from .forms import DateForm
from .models import FavDate

def index(request):
    # TODO: make this a real number:
    num_answers = FavDate.objects.count()
    context = {
        "title": "Basic Questions!",
        "num_answers": num_answers,
    }
    return render(request, "questionnaire/index.html", context)


def questionnaire(request):
    dateform = DateForm(request.POST or None)
    if dateform.is_valid():
        dateform.save()
        dateform = DateForm()
        return redirect('../')
    
    context = {
        "dateform": dateform,
    }
    return render(request, "questionnaire/questionnaire.html", context)

def results(request):
    favdate = FavDate.objects.all()
    # for obj in favdate:
    #     print(obj.month)
    #     print(obj.dayofweek)

    #--------------------------- Month Section --------------------------
    unique_date = dict()
    for date in favdate:
        if date.month in unique_date:
            unique_date[date.month] += 1
        elif date.month not in unique_date:
            unique_date[date.month] = 1

    sum_mon = sum(unique_date.values())

    percentage_mon = list()
    for i in unique_date.values():
        percentage_mon.append("{:.1f}".format(i/sum_mon*100))
    
    counter_mon = 0
    mon_info = list()
    for i,j in unique_date.items():
        mon_info.append((i, j, percentage_mon[counter_mon]))
        counter_mon += 1

    #--------------------------- Day Section ----------------------------
    unique_day = dict()
    for day in favdate:
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
    for z in unique_date.keys():
        day_to_mon[z] = dict()
    
    for m in favdate:
        mon_key = m.month
        day_key = m.dayofweek
        if day_key in day_to_mon[mon_key].keys():
            day_to_mon[mon_key][day_key] += 1
        elif day_key not in day_to_mon[mon_key].keys():
            day_to_mon[mon_key][day_key] = 1

    results = []
    for n in day_to_mon.keys():
        day_dict = day_to_mon[n]
        results.append([n, max(day_dict, key=day_dict.get)])

    context = {
        "mon_info": mon_info,
        "day_info": day_info,
        "results": results,
    }
    return render(request, "questionnaire/results.html", context)