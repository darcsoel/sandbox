class Foo:
    y = 1

    def __init__(self):
        self.x = 1

    @classmethod
    def class_foo(cls, x):
        cls.x = x
        cls.y = x


Foo.class_foo(4)

test = Foo()
test.class_foo(6)

Foo.class_foo(3)

test2 = Foo()

print(Foo.x)
print(test.x)
print(test2.x)

print(Foo.y)
print(test.y)
print(test2.y)
