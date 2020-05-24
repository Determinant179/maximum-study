import requests
import goslate
from bs4 import BeautifulSoup

def get_weather_data(city):
    gs = goslate.Goslate()
    query = gs.translate(city, "en")

    url = "https://yandex.ru/pogoda/" 
    responce = requests.get(url + query) 
    html = BeautifulSoup(responce.content, "lxml")

    temp = "температура: " + html.find("span", {'class': 'temp__value'}).text + '\n'
    condition = "состояние погоды: " + html.find("div", {'class': 'link__condition'}).text + '\n'
    pressure = "давление: " + html.find_all(class_="term__value")[4].text + '\n'
    humidity = "влажность: " + html.find_all(class_="term__value")[3].text + '\n'
    speed = "скорость ветра: " + html.find("span", {'class': 'wind-speed'}).text + '\n'

    return temp + condition + pressure + humidity + speed
