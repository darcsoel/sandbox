class Foo:
    def __init__(self):
        self.x = 1

    @staticmethod
    def static_foo(x):
        print(x)

    @classmethod
    def class_foo(cls, x):
        cls.x = x
        print(cls.x)


Foo.class_foo(4)
Foo.class_foo(3)

test = Foo()
test.class_foo(6)

Foo.class_foo(3)

test2 = Foo()

print(test.x)
print(test2.x)
