import vk_api
import parser

token = "828661df2658bb66c440aa4d19bb4e3df4befb4c008fb8ab7a52f300116906fa6424b7ced2c4645256f1e"

vk = vk_api.VkApi(token = token)
vk._auth_token()

while True:
    params = {"count" : 20, "filter" : "unanswered"}
    messages = vk.method("messages.getConversations", params)
    if messages["count"] > 0:

        id = messages["items"][0]["last_message"]["from_id"]
        message_id = messages["items"][0]["last_message"]["id"]
        
        message_text = messages['items'][0]['last_message']['text']

        if message_text == "курс доллара":
            answer_params = {"peer_id" : id, "random_id" : message_id, "message" : "Доллар: " + parser.getCourse('R01235')}
            vk.method("messages.send", answer_params)
        elif message_text == "курс белорусского рубля":
            answer_params = {"peer_id" : id, "random_id" : message_id, "message" : "Белорусский рубль: " + parser.getCourse('R01090B')}
            vk.method("messages.send", answer_params)
        else: 
            answer_params = {"peer_id" : id, "random_id" : message_id, "message" : "команда не распознана"}
            vk.method("messages.send", answer_params)