from inspect import Parameter, Signature


class Structure:
    _fields = []

    def __init__(self, *args):
        for key, value in zip(self._fields, args):
            setattr(self, key, value)


class SomeObj(Structure):
    _fields = ['first', 'second', 'third']


x = SomeObj(1, 2, 3)
print(x.__dict__)


def make_signature(names):
    return Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
                      for name in names])


class StructureRefactored:
    _signature = make_signature([])

    def __init__(self, *args, **kwargs):
        bound = self._signature.bind(*args, **kwargs)
        for key, value in bound.arguments.items():
            setattr(self, key, value)


class SomeObjRefactored(StructureRefactored):
    _signature = make_signature(['first', 'second', 'third'])


x = SomeObjRefactored(1, 2, 3)
print(x.__dict__)

# will throw TypeError
# x = SomeObjRefactored(first='1')
# print(x.__dict__)
