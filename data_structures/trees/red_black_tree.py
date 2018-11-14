BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'


class Nil:
    def __init__(self):
        self.color = BLACK
        self.value, self.left_child, self.right_child = None, None, None


class Node:
    def __init__(self, color=RED, value=None, left_child=None, right_child=None):
        self.color = color
        self.value = value
        self.left_child = left_child if left_child else Nil()
        self.right_child = right_child if right_child else Nil()


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value=int, node=None):
        if node is None:
            node = self.root

        if self._case1(value):
            return

        if self._case2(value, node):
            return

    def _case1(self, value):
        if self.root is None:
            self.root = Node(value=value, color=BLACK)
            return True

        return False

    def _case2(self, value, parent_node):
        if parent_node.color is RED:
            return False

        if value > parent_node.value:
            if parent_node.right_child is not Nil:
                self._case2(value, parent_node.right_child)
            else:
                parent_node.right_child = Node(value=value)
        else:
            if parent_node.left_child is not Nil:
                self._case2(value, parent_node.left_child)
            else:
                parent_node.left_child = Node(value=value)

        return True

    def _case3(self, value, parent_node):
        pass