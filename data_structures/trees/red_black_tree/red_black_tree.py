"""Red-Black tree implementation"""

import logging
from random import sample

from data_structures.trees.red_black_tree.env import BLACK, LEFT_ROTATION, \
    RIGHT_ROTATION
from data_structures.trees.red_black_tree.node import Node

logging.basicConfig(filename='red-black_tree.log', filemode='w+',
                    format='%(name) - $(levelname) - %(message)')


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
        self.balance(node)

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

    def balance(self, node):
        """Balance tree after add/delete"""

        pass

    def _case1(self, node: Node):
        """
        Case if node is root

        :param node: Node
        :return: None
        """
        if self.root is None:
            node.color = BLACK
            self.root = node
            return

        self._case2(node)

    def _case2(self, node: Node):
        """
        Case if father is black

        :param node: Node
        :return: None
        """

        if self.root is None:
            raise ValueError('root element is not defined')

        if node > node.parent.value:
            if node.parent.right_child.value is not None:
                self._case2(node.parent.right_child)
            else:
                node.parent.right_child = Node(value=node)
                return
        else:
            if node.parent.left_child.value is not None:
                self._case2(node.parent.left_child)
            else:
                node.parent.left_child = Node(value=node)
                return

        self._case3(node)

    def _case3(self, value, parent_node=None):
        """
        Case if father and uncle are red
        Recolor both to black and recolor grandfather

        :param node: Node
        :return: None
        """
        pass

    def _case4(self, value):
        """
        Father if red, uncle is black
        New node is right child, parent is left child
        Make left rotate

        :param node: Node
        :return: None
        """
        pass

    def _case5(self, value):
        """
        Father if red, uncle is black
        New node is left child, parent is left child
        Make right rotate with grandfather

        :param node: Node
        :return: None
        """
        pass

    @staticmethod
    def _rotate(node: Node, direction: str = 'left') -> None:
        """
        Rotate peace of tree
        Child and direction is linked, depends on direction

        :param node: center node to rotate, parent-(node)-child
        :param direction: -1 - left, 1 - right
        :return: None
        """
        if direction == LEFT_ROTATION:
            parent = node.parent
            rotator = node
            child = node.right_child

            parent.left_child = child
            child.left_child = rotator
        elif direction == RIGHT_ROTATION:
            parent = node.parent
            rotator = node
            child = node.left_child

            parent.left_child = child
            child.left_child = rotator
        else:
            msg = 'unknown rotation direction'
            logging.error(f'msg. supported options: {LEFT_ROTATION}, '
                          f'{RIGHT_ROTATION}')
            raise ValueError(msg)


if __name__ == '__main__':
    rb_tree = RedBlackTree()
    values = sample(range(1, 50), 20)

    for numb in values:
        rb_tree.insert(numb)
