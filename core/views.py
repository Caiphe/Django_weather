from django.shortcuts import render
from .forms import weatherForm
from .models import WeatherData
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests
import json

API_KEY = settings.WEATHER_API_KEY

@login_required(login_url='/')
def home(request):
    city_data = []
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}"
    if request.method == 'POST':
        form = weatherForm(request.POST)
        if form.is_valid():
            form.save()

    form = weatherForm

    get_city_data = WeatherData.objects.filter().order_by('-date_time').first()
    if get_city_data:
        city = get_city_data.city
        r = requests.get(url.format(city, API_KEY)).json()

        city_data = {
            'city': city,
            'temp': r['main']['temp'],
            'temp_min' : r['main']['temp_min'],
            'temp_max': r['main']['temp_max'],
            'humidity' : r['main']['humidity'],
            'description': r['weather'][0]['description'],
        }

    context = {
        'form' : form,
        'city_data': city_data
    }

    return render(request, 'core/index.html', context)

