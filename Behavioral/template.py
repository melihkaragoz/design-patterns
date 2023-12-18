class AbstractClass:
    def template_method(self):
        self.operation1()
        self.operation2()

    def operation1(self):
        pass

    def operation2(self):
        pass

class ConcreteClass(AbstractClass):
    def operation1(self):
        print("ConcreteClass: Operation 1 implementation")

    def operation2(self):
        print("ConcreteClass: Operation 2 implementation")

concrete_object = ConcreteClass()
concrete_object.template_method()
