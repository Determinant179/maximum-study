import os
from pygame import mixer
from gtts import gTTS

line = str(input("Введите текст для озвучивания: "))

my_file = open("speach.txt", "a")
my_file.write(line)
my_file.close()

mixer.init()

sth = gTTS(text = line, lang = 'en')
sth.save('audio.mp3')

mixer.music.load('audio.mp3')
mixer.music.play()
os.remove('audio.mp3')