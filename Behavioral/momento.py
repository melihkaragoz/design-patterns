class TextMemento:
    def __init__(self, text):
        self.text = text


class TextEditor:
    def __init__(self):
        self.text = ""

    def write_text(self, text):
        self.text += text

    def save_to_memento(self):
        return TextMemento(self.text)

    def restore_from_memento(self, memento):
        self.text = memento.text


class History:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_last_memento(self):
        if self.mementos:
            return self.mementos.pop()
        return None



text_editor = TextEditor()
history = History()

text_editor.write_text("This is a text. \t")

history.add_memento(text_editor.save_to_memento())
text_editor.write_text("New text. \t")

print("[Current Text]\t\t\t", text_editor.text)

last_memento = history.get_last_memento()
text_editor.restore_from_memento(last_memento)

print("[Text after restoration]\t", text_editor.text)