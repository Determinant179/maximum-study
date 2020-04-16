import requests
from bs4 import BeautifulSoup

city = "moscow"
url = "https://yandex.ru/pogoda/"
response = requests.get(url+city)

html = BeautifulSoup(response.content, "lxml")

print(html)

def main():
    pass