class Command:
    def execute(self):
        pass

class CreateCommand(Command):
    def __init__(self, server):
        self._server = server

    def execute(self):
        self._server.perform_action()

class Server:
    def perform_action(self):
        print("Action performed")

class Client:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def invoke(self):
        self._command.execute()

server = Server()
command = CreateCommand(server)
client = Client()

client.set_command(command)
client.invoke()
