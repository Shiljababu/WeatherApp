from django.shortcuts import render
import requests

from WeatherProject import settings



def weather_view(request):
    API_KEY = settings.OPENWEATHERMAP_API_KEY  # Replace with your OpenWeatherMap API key
    city = request.GET.get('city', 'Ernakulam')  # Default city

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    context = {}
    if response.status_code == 200:  # API call successful
        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
    else:
        context['error'] = "City not found. Try another!"

    return render(request, 'WeatherApp/home.html', context)
