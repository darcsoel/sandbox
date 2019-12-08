class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        left = self.left_child.value if self.left_child else None
        right = self.right_child.value if self.right_child else None

        return '(< {0} - {1} - {2} >)'.format(left, self.value, right)


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, value: Node, insert_to: Node):
        if self._root is None:
            self._root = value
        else:
            if insert_to is None:
                insert_to = self._root

            if value > insert_to.value:
                if insert_to.right_child is None:
                    insert_to.right_child = Node(value)
                else:
                    self.insert(value, insert_to.right_child)
            else:
                if insert_to.left_child is None:
                    insert_to.left_child = Node(value)
                else:
                    self.insert(value, insert_to.left_child)

