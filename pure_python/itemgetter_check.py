class ItemHolder:
    def __init__(self, items: dict):
        self.__items = items

    def __getitem__(self, item):
        if self.__items.get(item):
            return self.__items[item]
        else:
            return 'hello'


some_dict = {1: 'x', 2: 'e', 3: 'c'}

holder = ItemHolder(some_dict)

print(holder[0])
print(holder[2])
print(holder[3])
