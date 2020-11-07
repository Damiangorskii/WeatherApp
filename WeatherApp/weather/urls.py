from django.urls import path, include
from .views import home_view, detail_city_weather_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<city>', detail_city_weather_view, name='detail-city-weather'),
]
