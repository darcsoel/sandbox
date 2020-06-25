class TestObj:
    def __init__(self):
        self.x = 'str calling'
        self.y = 'repr calling'

    def __repr__(self):
        return self.y


class TestObj1:
    def __init__(self):
        self.x = 'str calling'
        self.y = 'repr calling'

    def __str__(self):
        return self.x

    def __repr__(self):
        return self.y


test = TestObj()
test1 = TestObj1()

print(test)
print(test1)

