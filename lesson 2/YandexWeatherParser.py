import requests
from bs4 import BeautifulSoup

city = "moscow" 
url = "https://yandex.ru/pogoda/" 
responce = requests.get(url + city) 
html = BeautifulSoup(responce.content, "lxml")

def temp(): 
    return html.find("span", {'class': 'temp__value'}).text

def condition(): 
    return html.find("div", {'class': 'link__condition'}).text

def time(): 
    time_now = html.find("time", {'class': 'time'}).text 
    time_now = time_now[7:12]
    time_now = int(time_now[0:2])*60+int(time_now[3:])

    sunrice = 60 * 6 
    sunset = 60 * 19 
    if time_now >= sunset or time_now < sunrice: 
        return "\U0001F31A" 
    elif time_now >= sunrice and time_now < sunset: 
        return "\U0001F31E"

def pressure():
    return html.find_all(class_="term__value")[4].text

def humidity():
    return html.find_all(class_="term__value")[3].text

def speed():
     return html.find("span", {'class': 'wind-speed'}).text  


def main():
    temp_value = temp()
    condition_value = condition()
    time_value = time()
    pressure_value = pressure()
    wind_value = speed()
    humidity_value = humidity()
    print("температура: ", temp_value)
    print("состояние погоды: ", condition_value)
    print("время: ", time_value)
    print("давление: ", pressure_value)
    print("влажность: ", humidity_value)
    print("скорость ветра: ", wind_value)
        
main()