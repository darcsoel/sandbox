import unittest

from labs.merge_k_sorted_lists import ListNode, SimpleSolution


class MyTestCase(unittest.TestCase):
    def test_1(self):
        llist1 = ListNode(1, next_=ListNode(4, next_=ListNode(5)))
        llist2 = ListNode(1, next_=ListNode(3, next_=ListNode(4)))
        llist3 = ListNode(2, next_=ListNode(6))

        result = SimpleSolution().mergeKLists([llist1, llist2, llist3])
        self.assertEqual(result.to_list(), [1, 1, 2, 3, 4, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
