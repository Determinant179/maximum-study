import requests 
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today()
today = today.strftime("%d/%m/%Y")
dictionary = {"date_req":today}

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

response = requests.get(url, params=dictionary)

xml = BeautifulSoup(response.content, "lxml")

def getCourse(jora):
    return xml.find("valute", {'id': jora}).value.text

print(getCourse("R01810"), " Южноафриканских рэндов")