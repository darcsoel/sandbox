import unittest

from data_structures.trees.red_black_tree import red_black_tree


class ThreeElementsBaseTestCase(unittest.TestCase):
    def insert_into_empty_tree(self, result, expected):
        red_black_tree.RedBlackTree()


if __name__ == '__main__':
    unittest.main()
