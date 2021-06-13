from typing import List

from labs.merge_two_sorted_lists import (ListNode,
                                         Solution as MergeTwoArraysSolution)


class SimpleSolution(MergeTwoArraysSolution):
    def __init__(self):
        self._result = None

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = None

        while lists:
            current = lists.pop()

            if not root:
                root = current
                continue

            root = self.mergeTwoLists(root, current)

        return root


class Solution(MergeTwoArraysSolution):
    def __init__(self):
        self._result = None

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None
