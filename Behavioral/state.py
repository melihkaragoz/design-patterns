class State:
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("Handling state A")

class ConcreteStateB(State):
    def handle(self):
        print("Handling state B")

class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        self._state.handle()

state_a = ConcreteStateA()
state_b = ConcreteStateB()

context = Context(state_a)
context.request()

context.set_state(state_b)
context.request()
