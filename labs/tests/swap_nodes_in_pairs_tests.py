import unittest

from labs.swap_nodes_in_pairs import ListNode, Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nodes = ListNode(1, next_=ListNode(2,
                                           next_=ListNode(3,
                                                          next_=ListNode(4))))
        sol = Solution().swapPairs(nodes)
        self.assertEqual(sol.to_list(), [2, 1, 4, 3])

    def test_2(self):
        nodes = ListNode(1, next_=ListNode(2, next_=ListNode(3)))
        sol = Solution().swapPairs(nodes)
        self.assertEqual(sol.to_list(), [2, 1, 3])

    def test_3(self):
        nodes = ListNode(1)
        sol = Solution().swapPairs(nodes)
        self.assertEqual(sol.to_list(), [1])


if __name__ == '__main__':
    unittest.main()
