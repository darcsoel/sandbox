import copy
import sys


class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self, name, obj):
        self.objects[name] = obj

    def unregister(self, name):
        try:
            del self.objects[name]
        except KeyError:
            pass

    def clone(self, name):
        return copy.deepcopy(self.objects[name])


if __name__ == '__main__':
    ob = {'field': 'value'}
    prot = Prototype()
    prot.register('test', ob)

    ob2 = prot.clone('test')
    print(ob2)
    sys.exit()
