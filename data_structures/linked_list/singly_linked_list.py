class ListItem:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, link):
        self.__next = link


class ListEntity:
    def __init__(self, root: ListItem):
        self.__root = root

    def add(self, node):
        if self.__root is None:
            self.__root.next = node
        else:
            next = self.__root

            while True:
                if next.next is None:
                    next = node
                    break
                else:
                    next = next.next


first_node = ListItem('test1')
second_node = ListItem('test2')
third_node = ListItem('test3')

linked_list = ListEntity(first_node)
linked_list.add(second_node)
linked_list.add(third_node)
