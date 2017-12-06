from Man import Man


class SuperMan(Man):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        print('It works')
