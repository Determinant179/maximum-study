import vk_api
import json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "828661df2658bb66c440aa4d19bb4e3df4befb4c008fb8ab7a52f300116906fa6424b7ced2c4645256f1e"
#токен бота!!!

vk = vk_api.VkApi(token = token)
vk._auth_token()

def keyboard():
    keyboard = VkKeyboard(one_time = False)
    keyboard.add_button('Белая кнопка', color = VkKeyboardColor.DEFAULT)
    keyboard.add_button('Зелёная кнопка', color = VkKeyboardColor.POSITIVE)
    keyboard.add_line() #Переход на новую строку
    keyboard.add_button('Красная кнопка', color = VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Синяя кнопка', color = VkKeyboardColor.PRIMARY)
    return keyboard.get_keyboard()

keyboard = keyboard()

while True:
    messages = vk.method("messages.getConversations", {"count" : 10, filter : "unansweared"})
    if messages["count"] >= 1:

        id = messages["items"][0]["last_message"]["from_id"]
        message_text = messages["items"][0]["last_message"]["text"]
        message_id = messages["items"][0]["last_message"]["id"]

        try: 
            if message_text == "начать":
                vk.method("messages.send", {"peer_id" : id, "random_id" : message_id, "message": "Выбери команду", "keyboard" : keyboard})
            elif message_text == "Белая кнопка":
                vk.method("messages.send", {"peer_id" : id, "random_id" : message_id, "message": "Вы нажали кнопку 1"})
            else: 
                vk.method("messages.send", {"peer_id" : id, "random_id" : message_id, "message": "Неизвестная команда"})
        except Exception:
            pass    
