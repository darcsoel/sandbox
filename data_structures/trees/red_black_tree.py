BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'


class Node:
    def __init__(self, color=BLACK, value=None, left_child=None, right_child=None):
        self.color = color
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value=value)
            return
