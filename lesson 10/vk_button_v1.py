import vk_api
import json

token = "828661df2658bb66c440aa4d19bb4e3df4befb4c008fb8ab7a52f300116906fa6424b7ced2c4645256f1e"
#токен бота!!!

vk = vk_api.VkApi(token = token)
vk._auth_token()

def get_button(label, color):
    return {
        "action" : {
            "type" : "text",
            "label" : label
        },
        "color" : color
    }

keyboard = {
    "one_time" : False,
    "buttons" : 
    [
        [
            get_button(label = "Кнопка 1", color = "positive"),
            get_button(label = "Кнопка 2", color = "negative"),
            get_button(label = "Кнопка 3", color = "primary"),
            get_button(label = "Кнопка 4", color = "secondary")
        ]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode("utf-8")
keyboard = str(keyboard.decode("utf-8"))

while True:
    messages = vk.method("messages.getConversations", {"count" : 10, filter : "unansweared"})
    if messages["count"] >= 1:

        id = messages["items"][0]["last_message"]["from_id"]
        message_text = messages["items"][0]["last_message"]["text"]
        message_id = messages["items"][0]["last_message"]["id"]

        try: 
            if message_text == "начать":
                vk.method("messages.send", {"peer_id" : id, "random_id" : message_id, "message": "Выбери команду", "keyboard" : keyboard})
            elif message_text == "Кнопка 1":
                vk.method("messages.send", {"peer_id" : id, "random_id" : message_id, "message": "Вы нажали кнопку 1"})
            else: 
                vk.method("messages.send", {"peer_id" : id, "random_id" : message_id, "message": "Неизвестная команда"})
        except Exception:
            pass    
