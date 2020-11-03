from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.

def home(request):

    query = request.GET.get('city')

    if query:


        url = 'http://api.openweathermap.org/data/2.5/weather?q='+query+'&APPID=d15a8e835c366afc687227da39ceb337'
        city = query

        r = requests.get(url.format(city)).json()
        

        weather_data = {
            'city': city,
            'temperature': round((int(r['main']['temp'])-273.15),1),
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        context = {
            'weather_data': weather_data,
        }

        return render(request, 'weather/weather_result.html', context)
    return render(request, 'home.html', {})
