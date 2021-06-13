class ListNode:
    def __init__(self, val=None, next_=None):
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
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = root = ListNode()

        while True:
            try:
                next_ = ListNode(head.next.val)
            except AttributeError:
                next_ = None

            try:
                current = ListNode(head.val)
            except AttributeError:
                break

            if current and next_:
                cur.next = next_
                cur.next.next = cur = current
            else:
                cur.next = current
                break

            try:
                head = head.next.next
            except AttributeError:
                break

        return root.next
