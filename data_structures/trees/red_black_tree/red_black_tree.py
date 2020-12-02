from random import sample

from .env import BLACK
from .node import Node


class RedBlackTree:
    """
    Red-black tree implementation
    """

    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        """
        Insert value to tree

        :param value:
        :return:
        """

        node = Node(value=value)
        self._case1(node)

    def find(self, node) -> Node:
        """
        Find node with needed value

        :param node: search value
        :return: Node
        """
        if node.parent_node is None:
            parent_node = self.root
        else:
            parent_node = node.parent

        if node < parent_node:
            return self.find(node.left_child)
        elif node > parent_node:
            return self.find(node.right_child)

        if node == parent_node:
            return parent_node

        raise KeyError('Value not exist')

    def _case1(self, node: Node):
        """
        Case if node is root

        :param node: int
        :return: None
        """
        if self.root is None:
            node.color = BLACK
            self.root = node
            return

        self._case2(node)

    def _case2(self, node: Node, parent_node: Node = None) -> bool:
        """
        Case if father is black

        :param node: int
        :param parent_node: Node | None
        :return: bool
        """
        if self.root is None:
            raise ValueError('root element is not defined')

        if parent_node is None:
            parent_node = self.root

        if node > parent_node.value:
            if parent_node.right_child.value is not None:
                self._case2(node, parent_node.right_child)
            else:
                parent_node.right_child = Node(value=node, parent=parent_node)
        else:
            if parent_node.left_child.value is not None:
                self._case2(node, parent_node.left_child)
            else:
                parent_node.left_child = Node(value=node, parent=parent_node)

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

    def _case4(self, value):
        """
        Father if red, uncle is black
        New node is right child, parent is left child
        Make left rotate

        :param value: int
        :param parent_node: Node
        :return: None
        """
        pass

    def _case5(self, value):
        """
        Father if red, uncle is black
        New node is left child, parent is left child
        Make right rotate with grandfather

        :param value: int
        :param parent_node: Node
        :return: None
        """
        pass

    @staticmethod
    def _rotate(node: Node, direction: int = -1) -> None:
        """
        Rotate peace of tree
        Child and direction is linked, depends on direction

        :param node: center node to rotate, parent-(node)-child
        :param direction: -1 - left, 1 - right
        :return: None
        """
        if direction < 0:
            parent = node.parent
            rotator = node
            child = node.right_child

            parent.left_child = child
            child.left_child = rotator
        else:
            parent = node.parent
            rotator = node
            child = node.left_child

            parent.left_child = child
            child.left_child = rotator


if __name__ == '__main__':
    rb_tree = RedBlackTree()
    values = sample(range(1, 50), 20)

    for numb in values:
        rb_tree.insert(numb)
