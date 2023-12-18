class Element:
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

class Visitor:
    def visit_concrete_element_a(self, element_a):
        pass

    def visit_concrete_element_b(self, element_b):
        pass

class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element_a):
        print("Visitor is processing ConcreteElementA")

    def visit_concrete_element_b(self, element_b):
        print("Visitor is processing ConcreteElementB")

elements = [ConcreteElementA(), ConcreteElementB()]
visitor = ConcreteVisitor()

for element in elements:
    element.accept(visitor)
