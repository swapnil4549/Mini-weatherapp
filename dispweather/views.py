import requests
from django.shortcuts import render
from django import forms
from django.http import HttpResponse


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=d570ec31bdcca0818995d2aebc0fea47'
    
    city =request.POST.get('city')
    
    op = requests.get(url.format(city)).json()
    temp = int(round(((op['main']['temp']) - 273.15),2))
    mintemp = round(((op['main']['temp_min']) - 273.15),2)
    maxtemp = round(((op['main']['temp_max']) - 273.15),2)
    city_data = {
        'city':city,
        'temperature':temp,
        'mintemp':mintemp,
        'maxtemp':maxtemp,
        'description':op['weather'][0]['description'],
        'icon':op['weather'][0]['icon']
        }
    data = {'city_data':city_data}
    return render(request,'home.html',data)
    
    
            


# Create your views here.
