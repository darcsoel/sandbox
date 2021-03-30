"""
You are given two non-empty linked lists representing two non-negative
integers.
The digits are stored in reverse order, and each of their nodes contains
a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
"""

# leetcode version

# class Solution:
#     def addTwoNumbers(self, first_l: ListNode, second_l: ListNode)
#     -> ListNode:
#         result = []
#         over_limit = 0
#
#         first = first_l
#         second = second_l
#
#         while True:
#             f = first.val if first else 0
#             s = second.val if second else 0
#             sum_ = f + s
#
#             if over_limit:
#                 sum_ += 1
#                 over_limit = 0
#
#             if sum_ > 9:
#                 sum_ -= 10
#                 over_limit = 10
#
#             result.append(sum_)
#
#             if (first is None or first.next is None) and (
#                     second is None or second.next is None):
#                 break
#             else:
#                 first = first.next if first else None
#                 second = second.next if second else None
#
#         while over_limit > 10:
#             result.append(0)
#             over_limit -= 10
#
#         if over_limit:
#             result.append(1)
#
#         node = None
#         for i in reversed(result):
#             if not node:
#                 node = ListNode(i, next=None)
#             else:
#                 node = ListNode(i, next=node)
#
#         return node


# Definition for singly-linked list.
from itertools import zip_longest


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = self._set_listed_value(val)
        self.next = next_

    def _set_listed_value(self, val) -> list:
        listed = []
        while val:
            temp = val % 10
            listed.append(temp)
            val //= 10

        return listed

    def __add__(self, other):
        result = []
        over_limit = 0

        for first, second in zip_longest(self.val, other.val):
            first = first or 0
            second = second or 0

            sum_ = first + second

            if over_limit:
                sum_ += 1
                over_limit = 0

            if sum_ > 9:
                sum_ -= 10
                over_limit = 10

            result.append(sum_)

        while over_limit > 10:
            result.append(0)
            over_limit -= 10

        if over_limit:
            result.append(1)

        mul = 1
        res_int = 0
        for i in result:
            res_int += i * mul
            mul *= 10

        print(result)
        return result


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return l1 + l2
