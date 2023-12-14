from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, msg):
        pass
 

class CreateObserver(Observer):
    _name = None

    def __init__(self, name):
        self._name = name

    def update(self, msg):
        print(f"[NOTIFY](for {self._name}) {msg}")


class Observable:
    _observers = []
    def __init__(self, state):
        self._state = state
        
    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        try:
            self._observers.remove(observer)
        except:
            pass

    def notify(self, msg):
        for obs in self._observers:
            obs.update(msg)


class CreateObservable(Observable):

    def set_state(self, state):
        self._state = state
        self.notify(state)

    def get_state(self):
        return f"current state: {self._state}"

# Create an Observable object 
work = CreateObservable("init")

# Create Observers to observe Observable object
worker = CreateObserver("John")
chef = CreateObserver("Jenny")

# Add observers to Observable's osbervers list
work.add_observer(worker)
work.add_observer(chef)

# Print Observable object's current state
print(work.get_state())

# Change observable object's state and print it
work.set_state("started to work")
print(work.get_state())
