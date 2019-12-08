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
            founded, parent = self.find(value)
        except KeyError as e:
            return e.args[0]

        if founded.left_child is None and founded.right_child is None:
            founded.value = None
        elif founded.left_child is None:
            if parent.left_child.value == value:
                parent.left_child = founded.right_child
            else:
                parent.right_child = founded.right_child
        elif founded.right_child is None:
            if parent.left_child.value == value:
                parent.left_child = founded.left_child
            else:
                parent.right_child = founded.left_child
        else:
            parent = founded
            successor = founded.right_child
            while successor.left_child:
                parent = successor
                successor = successor.left_child
            founded.value = successor.value

            if parent.left_child == successor:
                parent.left_child = successor.right_child
            else:
                parent.right_child = successor.right_child

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
        except KeyError as e:
            searched = e.args[0]

        print("Find element '{0}' - {1}".format(element, searched))

