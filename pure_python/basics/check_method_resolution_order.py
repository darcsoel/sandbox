class A:
    def __init__(self):
        self.message = 'first'

    def check(self):
        return self.message


class B:
    def __init__(self):
        self.message = 'second'

    def check(self):
        return self.message


class C(A, B):
    def __init__(self):
        super().__init__()


class Parent:
    def check(self):
        return 'hello'


class Child(Parent):
    def check(self):
        return super().check()


class Mock(Parent):
    def check(self):
        return 'mocked'


class Mock2:
    def check(self):
        return 'mocked2'


class CheckMro(Child, Mock):
    pass


class CheckMro2(Child, Mock2):
    pass


if __name__ == '__main__':
    print(C().check())
    print(CheckMro().check())
    print(CheckMro2().check())
