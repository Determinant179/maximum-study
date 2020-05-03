import telebot
from pygame import mixer
from gtts import gTTS

token = "1207310856:AAHPonzmeNABzWV3kxNFLiPfIiq_02_ji6E"

bot = telebot.TeleBot(token)

def get_json():
    return bot.get_updates()

def get_lastData(upd):
    return upd[-1]

def get_messageText(last_data):
    return last_data.message.text

def get_dialogID(last_data):
    return last_data.message.chat.id

def get_name(last_data):
    return last_data.message.chat.first_name + " " + last_data.message.chat.last_name

message_id = 0

while True:
    upd = get_json()
    data = get_lastData(upd)

    last_speaker = ""
    last_message = ""

    last_message_id = data.message.message_id

    text = get_messageText(data)
    dialod_id = get_dialogID(data)
    name = get_name(data)


    if last_message_id != message_id:
        message_id = last_message_id

        last_speaker = name
        last_message = text

        print(last_speaker + ":")
        print(last_message + '\n')

        if text == "привет":
            last_speaker = "bot"
            last_message = "Hello, " + name

            mixer.init()
            sth = gTTS(text = last_message, lang = 'en')
            sth.save('audio.mp3')

            audio = open('audio.mp3', 'rb')
            bot.send_voice(dialod_id, audio)
            print(last_speaker + ":")
            print(last_message + '\n')

        elif text == "пока":
            last_speaker = "bot"
            last_message = "До скорой встречи, " + name
            bot.send_message(dialod_id, last_message)
            print(last_speaker + ":")
            print(last_message + '\n')

        elif text == "отправь фотку котёнка":
            last_speaker = "bot"
            img = open("kitty.png", "rb")
            bot.send_photo(dialod_id, img)
            print(last_speaker + ":")
            print("Бот отправил пользователю фотку кота" + '\n')

        

