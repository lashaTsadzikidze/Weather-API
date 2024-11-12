from django.http import HttpResponse, JsonResponse
from .serializer import CitySerializer
from rest_framework import status
from .models import City
import requests

# Create your views here.
def weather_function(request, city):
    api_key = '02cab1f10dcf02b419fad606dc1c1fb3'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        city_obj = City.objects.create(name=city, temperature=temperature, humidity=humidity, description=description)

        serializer = CitySerializer(city_obj)

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return HttpResponse('Unable to fetch data!', status=status.HTTP_400_BAD_REQUEST)