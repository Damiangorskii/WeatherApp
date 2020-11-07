from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

import requests
import datetime

# Create your views here.

def home_view(request):

    query = request.GET.get('q')
    

    if query:


        url = 'http://api.openweathermap.org/data/2.5/weather?q='+query+'&APPID=d15a8e835c366afc687227da39ceb337'
        city = query

        r = requests.get(url.format(city)).json()
        

        weather_data = {
            'city': r['name'],
            'country': r['sys']['country'],
            'temperature': round((int(r['main']['temp'])-273.15),1),
            'temperatureFeelsLike': round((int(r['main']['feels_like'])-273.15),1),
            'mainDescription': r['weather'][0]['main'],
            'icon': r['weather'][0]['icon'],
            'datetime': datetime.datetime.now(),
        }

        context = {
            'weather_data': weather_data,
        }


        return render(request, 'weather/city_weather.html', context)
    return render(request, 'home.html', {})


def detail_city_weather_view(request, city):

    url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=d15a8e835c366afc687227da39ceb337'
    r = requests.get(url.format(city)).json()
        

    weather_data = {
        'city': r['name'],
        'country': r['sys']['country'],
        'temperature': round((int(r['main']['temp'])-273.15),1),
        'temperatureFeelsLike': round((int(r['main']['feels_like'])-273.15),1),
        'mainDescription': r['weather'][0]['main'],
        'icon': r['weather'][0]['icon'],
        'datetime': datetime.datetime.now(),
        'pressure': r['main']['pressure'],
        'description': r['weather'][0]['description'],
        'humidity': r['main']['humidity'],
        'visibility': r['visibility'],
        'tempMin': r['main']['temp_min'],
        'tempMax': r['main']['temp_max'],
        'wind': r['wind']['speed'],
        'cloudiness': r['clouds']['all'],
        'sunrise': r['sys']['sunrise'],
        'sunset': r['sys']['sunset'],
        'timezone': r['timezone'],
        }
        
    context = {
            'weather_data': weather_data,
    }


    return render(request, 'weather/detail_city_weather.html', context)
