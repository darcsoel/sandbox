# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def to_list(self):
        result = []

        while self.val:
            result.append(self.val)
            self.val = self.next.val if self.next else False
            self.next = self.next.next if self.next else False

        return result


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = root = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = cur = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = cur = ListNode(l2.val)
                l2 = l2.next

        cur.next = l1 or l2
        return root.next
