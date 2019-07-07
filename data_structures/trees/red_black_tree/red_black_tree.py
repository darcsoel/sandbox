from random import sample
from .node import Node
from .env import *


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        """
        Insert value to tree

        :param value:
        :return:
        """

        node = Node(value=value, color=BLACK)

        if self._case1(node):
            pass

    def find(self, node, parent_node: Node = None) -> Node:
        """
        Find node with needed value

        :param node: search value
        :param parent_node: parent node, root default
        :return: Node
        """
        if parent_node is None:
            parent_node = self.root

        if node < parent_node:
            return self.find(node, parent_node.left_child)
        elif node > parent_node:
            return self.find(node, parent_node.right_child)

        if node == parent_node:
            return parent_node
        else:
            raise KeyError('Value not exist')

    def _case1(self, node: Node) -> bool:
        """
        Case if node is root

        :param node: int
        :return: None
        """
        if self.root is None:
            self.root = node
            return True

        return False

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
