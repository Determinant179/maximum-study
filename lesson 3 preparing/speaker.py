import os
from pygame import mixer
from gtts import gTTS

my_file = open("file.txt","r")
my_string = my_file.read()
my_file.close()

mixer.init()

tts=gTTS(text=my_string, lang='ru')
tts.save('speak.mp3')

mixer.music.load('speak.mp3')
mixer.music.play()
os.remove('speak.mp3')
