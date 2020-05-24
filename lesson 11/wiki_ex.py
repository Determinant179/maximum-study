import wikipedia

info = "russia"

print(wikipedia.summary(info)) #общая информация

print(wikipedia.search(info)) #все статьи, в названии которых есть наше слово

page = wikipedia.page(info)

print(page.title) #название статьи
print(page.url) #ссылка на страницу
print(page.content) #вся статья
print(page.links) #все ссылки со страницы

wikipedia.set_lang("ru") #устанавливает язык по умолчанию
print(wikipedia.summary("Россия"))