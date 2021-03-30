import unittest

from labs.add_two_numbers import ListNode, Solution


class MyTestCase(unittest.TestCase):
    def test_123_with_321(self):
        first = ListNode(123)
        second = ListNode(321)
        self.assertEqual(Solution().addTwoNumbers(first, second), [4, 4, 4])

    def test_312_with_321(self):
        first = ListNode(321)
        second = ListNode(321)
        self.assertEqual(Solution().addTwoNumbers(first, second), [2, 4, 6])

    def test_999_with_999(self):
        first = ListNode(999)
        second = ListNode(999)
        self.assertEqual(Solution().addTwoNumbers(first, second), [8, 9, 9, 1])

    def test_9999999_with_9999(self):
        first = ListNode(9999999)
        second = ListNode(9999)
        self.assertEqual(Solution().addTwoNumbers(first, second),
                         [8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == '__main__':
    unittest.main()
