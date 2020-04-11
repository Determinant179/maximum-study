from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
from gtts import gTTS
from pygame import mixer
import time


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

def getCourse(id):
	return xml.find("valute",  {'id': id}).value.text

course_info = Label(window, text="Курс на: " + today.replace('/', '.'), font="Arial 18")
course_info.place(y=150, x=90)

usd_course = Label(window, text="$ " + getCourse("R01235"), font="Arial 16")
usd_course.place(y=190, x=100)

eur_course = Label(window, text="€ " + getCourse("R01239"), font="Arial 16")
eur_course.place(y=230, x=100)

def voice_course():
	mixer.init() 
	mp3_name = "/Users/paveltravkin/Desktop/Maximum/python/lesson 4 preparinng/audio.mp3"
	valutes = [
	"за 1 доллар дают {} рублей".format(getCourse("R01235")[:-2]),
	"за 1 евро дают {} рублей".format(getCourse("R01239")[:-2])
	]
	for valute in valutes:
		tts=gTTS(text=valute, lang='ru')
		tts.save(mp3_name)
		mixer.music.load(mp3_name)
		mixer.music.play()
		time.sleep(3)

btn = Button(text="Озвучить",         
             background="#555",     
             foreground="#ccc",            
             font="Arial 16", 
             command=voice_course              
             )

btn.place(y=270, x=250)

window.mainloop()