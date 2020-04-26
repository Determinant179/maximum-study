import socket
import views

class Webserver():
    def __init__(self, port, urls):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #AF_INET - протокол IPv4 (пример: 127.0.0.0.1)
        #SOCK_STREAM - технолоия работы сервера 

        self.websocket = ("127.0.0.1", port) #127.0.0.1 - "я" на языке компьютера

        self.urls = urls # вложенные ссылки


    def start(self): #метод запуска сервера
        self.server_socket.bind(self.websocket) 
        #резервирует адрес в сети и привязывает наше приложение к этому адресу
        self.server_socket.listen() #начинает слушать все запросы
        while True:
            client_socket, addres = self.server_socket.accept() 
            #возвращает объект для работы с пользователем и его адрес 
            request = client_socket.recv(2048) 
            #выделяем память под запрос пользователя (2048 байт)

            response = self.server_responce(request.decode("utf-8"))
            #создаём строку ответа на запрос пользователя

            print(addres)
            print(response)
            client_socket.sendall(response.encode("utf-8")) 
            #отправляем ответ пользователю
            client_socket.close()
    
    def parse_request(self, request): 
        # определяет какую вложенную ссылку хочет пользователь
        url = request.split(" ")[1]
        return url

    def get_headers(self, url):
        # создание заголовков ответа
        if url in self.urls:
            return "HTTP/1.1 200 OK\n\n", 200
        else:
            return "HTTP/1.1 404 Not Found\n\n", 404

    def get_content(self, code, url):
        # создание ответа пользователю
        if code == 404:
            return "<h1>404 not found</h1>"
        elif code == 200:
            return self.urls[url]

    def server_responce(self, request):
        url = self.parse_request(request)
        headers, code = self.get_headers(url)
        body = self.get_content(code, url)
        return headers + body

if __name__ == '__main__':

    urls = {"/" : views.main(), "/about" : views.about()}

    server = Webserver(8004, urls)
    server.start()