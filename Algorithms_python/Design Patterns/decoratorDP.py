#test
class text:
    def __init__(self, text):
        self._text = text
    def render(self):
        return self._text

class underline(text):
    def __init__(self, text):
        self._text = text
    def render(self):
        return "<u>{}</u>".format(self._text.render())

print(text("Test").render())
print(underline(text("Test")).render())