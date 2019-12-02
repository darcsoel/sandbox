from data_structures.linked_list.list_item import ListItem


class LinkedList:
    def __init__(self, values=None):
        self._root = None
        if isinstance(values, (list, tuple)):
            for value in values:
                node = ListItem(value)
                self.push(node)
        elif values is not None:
            self.push(ListItem(values))

    def get_first_value(self):
        return self._root.value

    def get(self):
        if self._root is None:
            return

        values = []

        element = self._root

        while True:
            values.append(element.value)
            if element.next is None:
                break
            else:
                element = element.next

        return values

    def __len__(self):
        return len(self.get())

    def print(self):
        return print(self.get())
    
    def add(self, node: ListItem):
        node.next = self._root
        self._root = node
        
    def push(self, node: ListItem):
        if self._root is None:
            self._root = node
            return

        next_node = self._root

        while next_node.next:
            next_node = next_node.next

        next_node.next = node

    def pop(self):
        self._root = self._root.next

    def delete(self, node):
        if node is None or node.value is None:
            raise ValueError('Wrong node to delete')

        previous_to_delete = None
        to_delete = self._root

        while True:
            if to_delete.next is None:
                break

            if to_delete.value != node.value:
                previous_to_delete = to_delete
                to_delete = to_delete.next
            else:
                break

        if previous_to_delete:
            previous_to_delete.next = to_delete.next
        else:
            self._root = to_delete.next

        del to_delete


if __name__ == '__main__':
    first_node = ListItem('test1')
    second_node = ListItem('test2')
    third_node = ListItem('test3')
    forth_node = ListItem('test4')
    fifth_node = ListItem('test5')

    linked_list = LinkedList()
    linked_list.push(first_node)
    linked_list.push(second_node)
    linked_list.push(third_node)
    linked_list.push(forth_node)
    linked_list.push(fifth_node)

    linked_list.print()

    linked_list.pop()
    linked_list.print()

    linked_list.delete(second_node)
    linked_list.delete(forth_node)
    linked_list.print()

