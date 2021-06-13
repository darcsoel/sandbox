import unittest

from labs.reverse_nodes_in_k_groups import Solution
from labs.swap_nodes_in_pairs import ListNode


def generate_list_nodes(values):
    result = None

    for val in reversed(values):
        result = ListNode(val=val, next_=result)

    return result


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_1(self):
        nodes = generate_list_nodes([1, 2, 3, 4, 5])
        sol = Solution().reverseKGroup(nodes, 2)
        self.assertEqual(sol.to_list(), [2, 1, 4, 3, 5])

    def test_2(self):
        nodes = generate_list_nodes([1, 2, 3, 4, 5])
        sol = Solution().reverseKGroup(nodes, 3)
        self.assertEqual(sol.to_list(), [3, 2, 1, 4, 5])

    def test_3(self):
        nodes = generate_list_nodes([1, 2, 3, 4, 5])
        sol = Solution().reverseKGroup(nodes, 1)
        self.assertEqual(sol.to_list(), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
