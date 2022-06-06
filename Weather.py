import requests
import os


def get_weather(city):
    appid= os.environ['token']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&type=like&APPID={appid}&lang=ua&units=metric'
    r = requests.get(url)
    res = r.json()
    print()
    
    city = res ['name']
    description =res['weather'][0]['description']
    temp = res['main']['temp']
    humidity = res["main"]["humidity"]
    pressure = res["main"]["pressure"]
    wind = res["wind"]["speed"]

    print(f"Погода у місті: {city}\nХмарність: {description}\nТемпература:{temp}°C\n"
        f"Вологість: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {wind} м/с")

get_weather('donetsk')


