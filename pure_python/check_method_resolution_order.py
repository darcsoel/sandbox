class A:
    def __init__(self):
        self.message = 'first'

    def check(self):
        print(self.message)


class B:
    def __init__(self):
        self.message = 'second'

    def check(self):
        print(self.message)


class C(A):
    def __init__(self):
        super().__init__()
        self.message = 'third'

    def check(self):
        super().check() + print(self.message)


class Main(C, B):
    def run(self):
        self.check()


Main().run()
