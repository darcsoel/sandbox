class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        left = self.left_child.value if self.left_child else None
        right = self.right_child.value if self.right_child else None

        return '(< {0} - {1} - {2} >)'.format(left, self.value, right)

    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if value > self.value:
                if self.right_child is None:
                    self.right_child = Node(value)
                else:
                    self.right_child.insert(value)
            else:
                if self.left_child is None:
                    self.left_child = Node(value)
                else:
                    self.left_child.insert(value)

    def delete(self, value):
        try:
            finded, parent = self.find(value)
        except KeyError as err:
            return err.args[0]

        if finded.left_child is None and finded.right_child is None:
            finded.value = None
        elif finded.left_child is None:
            if parent.left_child.value == value:
                parent.left_child = finded.right_child
            else:
                parent.right_child = finded.right_child
        else:
            if parent.left_child.value == value:
                parent.left_child = finded.left_child
            else:
                parent.right_child = finded.left_child

        return True

    def find(self, value, parent=None):
        if self.value is None:
            raise KeyError('Value {0} not found'.format(value))

        if value > self.value and self.right_child:
            return self.right_child.find(value, self)
        elif value < self.value and self.left_child:
            return self.left_child.find(value, self)

        if self.value == value:
            return self, parent
        else:
            raise KeyError('Value {0} not found'.format(value))

    @staticmethod
    def print_tree(node):
        """ For simplify use defined root element """
        tree = []

        if node is not None:
            tree.append(node.value)
            tree += node.print_tree(node.left_child)
            tree += node.print_tree(node.right_child)

        return tree


def print_searched_values(node, elements):
    for element in elements:
        try:
            searched, _ = node.find(element)
        except KeyError as err:
            searched = err.args[0]

        print("Find element '{0}' - {1}".format(element, searched))


if __name__ == '__main__':
    values_for_input = [16, 6, 25, 2, 34, 54, 22, 4, 12, 15, 9]
    node = Node()

    for number in values_for_input:
        node.insert(number)

    print(node.print_tree(node))

    print_searched_values(node, [16, 25, 22, 34, 5, 9])

    print(node.delete(3))
    print(node.delete(9))
    print(node.delete(25))

    try:
        print(node.find(9))
        print(node.find(16))
    except KeyError as err:
        print(err.args[0])

    print_searched_values(node, [16, 25, 22, 5, 9])
