class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            print("Handler A handling the request")
        else:
            super().handle_request(request)

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            print("Handler B handling the request")
        else:
            super().handle_request(request)

handler_chain = ConcreteHandlerA(ConcreteHandlerB())
handler_chain.handle_request("A")
