import requests
from bs4 import BeautifulSoup

city = "moscow"
url = "https://yandex.ru/pogoda/"
response = requests.get(url+city)

html = BeautifulSoup(response.content, "lxml")

def temp():
    return html.find("span", {'class': 'temp__value'}).text


def main():
    temp_value = temp()
    print(temp_value)

main()