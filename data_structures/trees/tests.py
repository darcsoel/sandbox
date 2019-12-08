import unittest

from data_structures.trees.binary_search_tree.binary_search_tree import Node as BinaryTreeNode


class BinaryTreeTest(unittest.TestCase):
    def setUp(self) -> None:
        node = BinaryTreeNode()
