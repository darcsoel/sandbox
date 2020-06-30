from dataclasses import dataclass


@dataclass
class ExampleDataClass:
    """
    Primitive dataclass
    """

    id: int
    value: str = 'default'


first = ExampleDataClass(1, "first")
second = ExampleDataClass(2, "second")
third = ExampleDataClass(3)

print(first)
print(second)
print(third)
print(first == second)
