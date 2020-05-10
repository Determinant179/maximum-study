import vk_api

token = "828661df2658bb66c440aa4d19bb4e3df4befb4c008fb8ab7a52f300116906fa6424b7ced2c4645256f1e"

vk = vk_api.VkApi(token = token)
vk._auth_token()

while True:
    params = {"count" : 20, "filter" : "unanswered"}
    messages = vk.method("messages.getConversations", params)
    if messages["count"] > 0:

        id = messages["items"][0]["last_message"]["from_id"]
        message_id = messages["items"][0]["last_message"]["id"]
        
        answer_params = {"peer_id" : id, "random_id" : message_id, "message" : "Окей"}
        vk.method("messages.send", answer_params)