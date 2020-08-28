class Foo:
    def __new__(cls, *args, **kwargs):
        print('New')
        super().__new__(cls)

    def __init__(self, x):
        print(f'Init {x}')
        super().__init__()


first = Foo('first')
second = Foo('second')

