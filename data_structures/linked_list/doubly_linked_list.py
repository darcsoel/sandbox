class DoubleLinkedItem:
    def __init__(self, value):
        self._value = value
        self._next = None
        self._previous = None

    @property
    def value(self):
        return str(self._value)

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, link):
        self._next = link

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, link):
        self._previous = link

    def __str__(self):
        return self.value


class DoubleLinkedList:
    def __init__(self):
        self._root = None
