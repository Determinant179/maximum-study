from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.geometry("380x500+300+300")
window.title("Курс валют")

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")

payload = {"date_req" : today}

responce = requests.get(url, params=payload)

xml = BeautifulSoup(responce.content, "lxml")

def getCourse (id):
	return xml.find("valute",  {'id': id}).value.text

course_USD = Label(window, text = "$ " + getCourse("R01235"), font = "Arial 18")
course_USD.place(y = 250, x = 90)

course_EUR = Label(window, text = "€ " + getCourse("R01239"), font = "Arial 18")
course_EUR.place(y = 300, x = 90)

course_today = Label(window, text = "Курс на " + today.replace('/', '.'), font = "Arial 18")
course_today.place(y=200, x = 90)

btc_url = "https://coinspot.io/currencies/view/btc"
btc_responce = requests.get(btc_url)
btc_xml = BeautifulSoup(btc_responce.content, "lxml")

def getCourse_btc():
    return btc_xml.find("span", {'class':'price'}).text

course_btc = Label(window, text = "₿ " + getCourse_btc(), font = "Arial 18")
course_btc.place(x = 90, y = 350)

img = PhotoImage(file = "logo.png")
pic = Label(window, image = img)
pic.place(x = 100, y = 20)

window.mainloop()