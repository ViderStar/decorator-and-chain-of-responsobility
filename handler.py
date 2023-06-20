from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, request):
        pass


class RequestHandler(Handler):
    def handle_request(self, request):
        if self.next_handler:
            return self.next_handler.handle_request(request)
        return f"Обработка запроса: {request}"


class Decorator(Handler):
    def __init__(self, handler):
        super().__init__(handler)

    def handle_request(self, request):
        if self.next_handler:
            return self.next_handler.handle_request(request)
        return


class RequestLogger(Decorator):
    def handle_request(self, request):
        print(f"Логирование запроса: {request}")
        return super().handle_request(request)


class RequestAuthorizer(Decorator):
    def handle_request(self, request):
        if request.get("token") == "secret":
            print("Запрос авторизован.")
            return super().handle_request(request)
        print("Запрос не авторизован.")
        return
