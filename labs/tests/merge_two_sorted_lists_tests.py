import unittest

from labs.merge_two_sorted_lists import ListNode, Solution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        llist1 = ListNode(1, next_=ListNode(2, next_=ListNode(4)))
        llist2 = ListNode(1, next_=ListNode(3, next_=ListNode(4)))
        result = Solution().mergeTwoLists(llist1, llist2)
        self.assertEqual(result.to_list(), [1, 1, 2, 3, 4, 4])


if __name__ == '__main__':
    unittest.main()
