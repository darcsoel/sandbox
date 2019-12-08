import unittest

from data_structures.trees.binary_search_tree.binary_search_tree import Node as BinaryTreeNode


class BinaryTreeTest(unittest.TestCase):
    def setUp(self) -> None:
        node = BinaryTreeNode()
        values_for_input = [16, 6, 25, 2, 34, 54, 22, 4, 12, 15, 9]

        for number in values_for_input:
            node.insert(number)

    def test_insert(self):
        pass

    def test_delete(self):
        pass
