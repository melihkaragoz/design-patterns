from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass

class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        if self.has_next():
            item = self.collection[self.index]
            self.index += 1
            return item
        else:
            return None

    def has_next(self):
        return self.index < len(self.collection)

# Aggregate interface
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.items = []

    def create_iterator(self):
        return ConcreteIterator(self.items)

    def add_item(self, item):
        self.items.append(item)

aggregate = ConcreteAggregate()
aggregate.add_item("Item 1")
aggregate.add_item("Item 2")
aggregate.add_item("Item 3")

iterator = aggregate.create_iterator()

while iterator.has_next():
    item = iterator.next()
    print(item)
