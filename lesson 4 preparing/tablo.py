from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.geometry("400x350+300+300")
window.title("Курс валют")

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req" : today}

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, "lxml")

def getCourse (id):
	return xml.find("valute",  {'id': id}).value.text


img_logo = PhotoImage(file='/Users/paveltravkin/Desktop/Maximum/python/lesson 4 preparinng/logo.png')
logo = Label(window, image=img_logo)
logo.place(x=0, y=0)

lab = Label(window, text="Курс валют \n MAXIMUM банк", fg="black", font="Arial 22")
lab.place(y=25, x=150)

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req" : today}

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, "lxml")

def getCourse (id):
	return xml.find("valute",  {'id': id}).value.text

course_info = Label(window, text="Курс на: " + today.replace('/', '.'), font="Arial 18")
course_info.place(y=150, x=90)

usd_course = Label(window, text="$ " + getCourse("R01235"), font="Arial 16")
usd_course.place(y=190, x=100)

eur_course = Label(window, text="€ " + getCourse("R01239"), font="Arial 16")
eur_course.place(y=230, x=100)

btc_url = "https://coinspot.io/currencies/view/btc"
btc_responce = requests.get(btc_url)
btc_xml = BeautifulSoup(btc_responce.content, "lxml")
btc = btc_xml.find("span",  {'class': 'price'}).text

btc = str(round(float(btc[2:]), 2))

eur_course = Label(window, text="₿ " + btc, font="Arial 16")
eur_course.place(y=270, x=100)


window.mainloop()
