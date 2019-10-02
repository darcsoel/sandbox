class SomeClass:
    def __init__(self, some_number):
        self.some_number = some_number

    def __call__(self, number):
        return number * self.some_number


x = SomeClass(6)
print(x(6))
