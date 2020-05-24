import wikipedia 

def get_summary(name): 
    try: 
        wikipedia.set_lang("ru") 
        page = wikipedia.page(name) 
        return "{0}\nБольше подробностей по ссылке - {1}".format(page.summary, page.url) 
    except Exception: 
        return " :( Страничка не найдена" 
        
