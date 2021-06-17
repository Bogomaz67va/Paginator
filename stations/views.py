from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    list_station = list()
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f_csv:
        reader = csv.DictReader(f_csv)
        for row in reader:
            list_station.append(row)
    page = int(request.GET.get("page", 1))
    elements_per_page = 10
    paginator = Paginator(list_station, elements_per_page)
    page_ = paginator.get_page(page)
    content = page_.object_list

    context = {
        'bus_stations': content,
        'page': page_,
    }

    return render(request, 'stations/index.html', context=context)
