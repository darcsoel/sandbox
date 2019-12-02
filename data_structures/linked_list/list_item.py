class ListItem:
    def __init__(self, value):
        self._value = value
        self._next = None

    @property
    def value(self):
        return str(self._value)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, link):
        self._next = link

    def __str__(self):
        return self.value
