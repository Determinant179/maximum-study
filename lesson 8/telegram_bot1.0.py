import telebot

token = "1207310856:AAHPonzmeNABzWV3kxNFLiPfIiq_02_ji6E"

bot = telebot.TeleBot(token)

upd = bot.get_updates() #данные обо всех диалогах и сообщениях

last_data = upd[-1] #записываем в переменную upd данные о последнем сообщении

last_message = last_data.message.text
print(last_message)

last_dialog_id = last_data.message.chat.id
print(last_dialog_id)

bot.send_message(last_dialog_id, "Привет, " + last_data.message.chat.first_name)

img = open('kitty.png', 'rb')
bot.send_photo(last_dialog_id, img)

bot.send_location(last_dialog_id, 55.756272, 37.652809)
