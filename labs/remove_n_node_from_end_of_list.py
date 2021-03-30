"""
Given the head of a linked list, remove the nth node from the end of
the list and return its head.
"""


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fake = ListNode(0)
        fake.next = head
        length = 0

        elem = head
        while elem:
            length += 1
            elem = elem.next

        elem = fake
        length -= n
        while length:
            elem = elem.next
            length -= 1

        elem.next = elem.next.next
        return fake.next
