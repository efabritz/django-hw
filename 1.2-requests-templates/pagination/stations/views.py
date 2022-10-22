from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def read_csv(csv_file, mode="r", encoding="utf-8-sig"):
    with open(csv_file) as file:
        data = csv.DictReader(file)
        bus_stations = [dict(item) for item in data]
    return bus_stations

DATA = read_csv('data-398-2018-08-30.csv')


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(DATA, 10)
    page = paginator.get_page(page_number)
    start = page.start_index() - 1
    end = page.end_index()
    bus_stations = DATA[start:end]

    context = {
        'bus_stations': bus_stations,
        'page': page
    }
    return render(request, 'stations/index.html', context)
