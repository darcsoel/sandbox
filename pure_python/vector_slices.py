import reprlib


class Vector:
    def __init__(self, range_):
        self._items = list(range_)

    def __repr__(self):
        components = reprlib.repr(self._items)
        return f'Vector: {components}'

    def __len__(self):
        return len(self._items)

    def __getitem__(self, item):
        cls = type(self)

        if isinstance(item, slice):
            return cls(self._items[item])
        elif isinstance(item, int):
            return self._items[:item]


vector = Vector(range(10))
print(vector)
print(vector[:2])

