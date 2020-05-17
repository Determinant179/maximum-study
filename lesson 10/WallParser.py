import vk_api

token = "aa825cffaa825cffaa825cffc4aaf3a189aaa82aa825cfff443535036fd414dd8f35514"

vk = vk_api.VkApi(token = token)
vk._auth_token()

posts = vk.method("wall.get", {"owner_id" : "-51324776", "offset" : "1", "count" : "10"})
#print(posts["items"][0]["text"])

for post in range(len(posts["items"])):
    print(posts["items"][post]["text"])
    try:
        print(posts["items"][post]["attachments"][0]["photo"]["sizes"][0]["url"])
    except Exception:
        pass
    print("_________________________________")