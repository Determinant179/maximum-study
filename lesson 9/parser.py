import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

dictionary = {"date_req" : today}
response = requests.get(url, params = dictionary)

xml = BeautifulSoup(response.content, "lxml")

def getCourse(id):
    return xml.find("valute", {"id" : id}).value.text