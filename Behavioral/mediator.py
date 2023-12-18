class Mediator:
    def notify(self, sender, event):
        pass

class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator

    def send(self, event):
        self._mediator.notify(self, event)

    def receive(self, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, colleague1, colleague2):
        self._colleague1 = colleague1
        self._colleague2 = colleague2

    def notify(self, sender, event):
        if sender == self._colleague1:
            self._colleague2.receive(event)
        else:
            self._colleague1.receive(event)

class ConcreteColleague(Colleague):
    def receive(self, event):
        print(f"Colleague received event: {event}")

colleague1 = ConcreteColleague(None)
colleague2 = ConcreteColleague(None)

mediator = ConcreteMediator(colleague1, colleague2)

colleague1._mediator = mediator
colleague2._mediator = mediator

colleague1.send("Event from colleague 1")
colleague2.send("Event from colleague 2")
