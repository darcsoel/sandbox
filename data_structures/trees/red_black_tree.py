from random import sample

BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'


class Nil:
    def __init__(self):
        self.color = BLACK
        self.value, self.left_child, self.right_child = None, None, None


class Node:
    def __init__(self, color=RED, value=None, left_child=None, right_child=None, parent=None):
        self.color = color
        self.value = value
        self.parent = parent
        self.left_child = left_child if left_child else Nil()
        self.right_child = right_child if right_child else Nil()


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        """
        Insert value to tree

        :param value:
        :return:
        """

        self._case1(value)

    def _case1(self, value) -> bool:
        """
        Case if node is root

        :param value: int
        :return: None
        """
        if self.root is None:
            self.root = Node(value=value, color=BLACK)
            return True

        return False

    def _case2(self, value, parent_node=None):
        """
        Case if father is black

        :param value: int
        :param parent_node: Node | None
        :return: bool
        """
        if self.root is None:
            raise ValueError('root element is not defined')

        parent_node = self.root

        if value > parent_node.value:
            if parent_node.right_child is not Nil:
                self._case2(value, parent_node.right_child)
            else:
                parent_node.right_child = Node(value=value, parent=parent_node)
        else:
            if parent_node.left_child is not Nil:
                self._case2(value, parent_node.left_child)
            else:
                parent_node.left_child = Node(value=value, parent=parent_node)

        return True

    def _case3(self, value, parent_node=None):
        """
        Case if father and uncle are red
        Recolor both to black and recolor grandfather

        :param value: int
        :param parent_node: Node | None
        :return: bool
        """
        pass

    def _case4(self, value, parent_node):
        """
        Father if red, uncle is black
        New node is right child, parent is left child
        Make left rotate

        :param value: int
        :param parent_node: Node
        :return: None
        """
        pass

    def _case5(self, value, parent_node):
        """
        Father if red, uncle is black
        New node is left child, parent is left child
        Make right rotate

        :param value: int
        :param parent_node: Node
        :return: None
        """
        pass

    def _rotate(self, node: Node, direction=-1):
        """
        Rotate peace of tree
        Child and direction is linked, depends on direction

        :param node: center node to rotate, parent-node-child
        :param direction: -1 - left, 1 - right
        :return: bool
        """
        pass


if __name__ == '__main__':
    rb_tree = RedBlackTree()
    values = sample(range(1, 50), 20)
    rb_tree.insert(value=1)
