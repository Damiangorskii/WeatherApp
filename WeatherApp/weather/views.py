from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from suntime import Sun, SunTimeException

import requests
import datetime
import time

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

    sunrise = ""
    sunset = ""

    latitude = r['coord']['lat']
    longitude = r['coord']['lon']


    sun = Sun(latitude, longitude)

    dt = datetime.datetime.today()

    #to fix: local time sunrise and sunset, error with KeyError or favicon.ico
    #https://github.com/SatAgro/suntime



    try:
        sunrise = sun.get_local_sunrise_time(dt)
        sunset = sun.get_local_sunset_time()
    except SunTimeException as e:
        print("Error: {0}.".format(e))



        

    weather_data = {
        'city': city,
        'country': r['sys']['country'],
        'temperature': round((int(r['main']['temp'])-273.15),1),
        'temperatureFeelsLike': round((int(r['main']['feels_like'])-273.15),1),
        'mainDescription': r['weather'][0]['main'],
        'icon': r['weather'][0]['icon'],
        'datetime': datetime.datetime.now(),
        'pressure': r['main']['pressure'],
        'description': r['weather'][0]['description'],
        'humidity': r['main']['humidity'],
        'visibility': round((int(r['visibility'])/1000),1),
        'tempMin': round((int(r['main']['temp_min'])-273.15), 1),
        'tempMax': round((int(r['main']['temp_max'])-273.15),1),
        'wind': r['wind']['speed'],
        'cloudiness': r['clouds']['all'],
        'sunrise': sunrise,
        'sunset': sunset,
        'timezone': (int(r['timezone'])/3600),
        }
        
    context = {
        'weather_data': weather_data,
    }


    return render(request, 'weather/detail_city_weather.html', context)
