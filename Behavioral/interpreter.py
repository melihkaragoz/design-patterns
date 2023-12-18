from abc import ABC, abstractmethod

class Context:
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_position = 0

    def current_token(self):
        return self.input_string[self.current_position]

    def next_token(self):
        self.current_position += 1

class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        if context.current_token() == 'A':
            context.next_token()
            return True
        else:
            return False

class NonTerminalExpression(AbstractExpression):
    def interpret(self, context):
        expression1 = TerminalExpression()
        expression2 = TerminalExpression()
        return expression1.interpret(context) and expression2.interpret(context)

context = Context("AA")
expression = NonTerminalExpression()

result = expression.interpret(context)
print(result)
