import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"
date = "date_req=28/08/2018"

today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req" : today}

responce = requests.get(url, params=payload)

print(responce.url)

xml = BeautifulSoup(responce.content, "lxml")

def getCourse (id):
	return xml.find("valute",  {'id': id}).value.text


print(getCourse("R01235"), "рублей за 1 доллар")
print(getCourse("R01239"), "рублей за 1 евро")
print(getCourse("R01375"), "рублей за 10 юаней")
