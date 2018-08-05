class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        left, right = None, None

        if self.left_child is not None:
            left = self.left_child.value
        if self.right_child is not None:
            right = self.right_child.value

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

    # todo complete this
    def delete(self, value):
        pass

    def find(self, value):
        if value > self.value and self.right_child:
            return self.right_child.find(value)
        elif value < self.value and self.left_child:
            return self.left_child.find(value)

        if self.value == value:
            return self
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


if __name__ == '__main__':
    values_for_input = [16, 6, 25, 2, 34, 54, 22, 4, 12, 15, 9]
    node = Node()

    for number in values_for_input:
        node.insert(number)

    print(node.print_tree(node))

    for element in [16, 34, 5, 9]:
        try:
            searched = node.find(element)
        except KeyError as err:
            searched = err.args[0]

        print("Find element '{0}' - {1}".format(element, searched))
