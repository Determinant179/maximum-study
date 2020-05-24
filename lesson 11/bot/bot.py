import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType

from bot_modules.weather import get_weather_data
from bot_modules.course import get_course
from bot_modules.wiki import get_summary




TOKEN = "828661df2658bb66c440aa4d19bb4e3df4befb4c008fb8ab7a52f300116906fa6424b7ced2c4645256f1e"

vk_session = vk_api.VkApi(token=TOKEN)


vk = vk_session.get_api()

upload = VkUpload(vk_session)
longpoll = VkLongPoll(vk_session)
hello = '''
Привет я Бот Ксюша, я всегда готова тебе помочь
-с <объект> - краткая справка о интересующем тебя объекте
-п <город> - погода в твоём городе
-к - курс валют
'''


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg_text = event.text
        msg_text = msg_text.replace(" ", "_")
        query = msg_text[3:]
        message_id = event.message_id

        if msg_text == "начать" or msg_text == "?":
            vk.messages.send(user_id=event.user_id, random_id=message_id, message=hello)

        elif msg_text[0:2] == "-с":
            vk.messages.send(user_id=event.user_id, random_id=message_id,  message=get_summary(query))

        elif msg_text[0:2] == "-п":
            try:
                response = get_weather_data(query)
            except Exception:
                response = ":( Сервис не доступен"

            vk.messages.send(user_id=event.user_id, random_id=message_id, message=response)

        elif msg_text[0:2] == "-к":
            response = "{0} рублей за 1 доллар \n {1} рублей за 1 евро \n {2} рублей за 10 юаней \n {3} рублей за фунт"
            response = response.format(get_course("R01235"), get_course("R01239"), get_course("R01375"), get_course("R01035"))
            vk.messages.send(user_id=event.user_id, random_id=message_id, message=response)

        else:
            vk.messages.send(user_id=event.user_id, random_id=message_id, message=hello)
