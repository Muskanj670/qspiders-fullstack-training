from django.shortcuts import render
import requests

api_key = "de8318900962669c1c75fd8cc1363bb2"
base_url = f"https://api.openweathermap.org/data/2.5/weather?q={{city_name}}&appid={{api_key}}&units=metric"

# Create your views here.

def today(request):
    city_name = 'Noida'
    if request.method == 'GET':
        city_name = request.GET.get('city')
    api_url = base_url.format(city_name=city_name, api_key=api_key)
    response = requests.get(api_url)
    weather_data = response.json()
    return render(request, 'myapp/today.html',{"weather_data": weather_data})


def joke(request):
    url  = "https://v2.jokeapi.dev/joke/Any?type=single"
    data = requests.get(url).json()
    return render(request, 'myapp/joke.html', {'joke': data['joke']})