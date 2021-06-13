"""
Given a linked list, reverse the nodes of a linked list k at a time and
return its modified list.

k is a positive integer and is less than or equal to the length of the
linked list. If the number of nodes is not a multiple of k then left-out
nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes
themselves may be changed.
"""

from labs.swap_nodes_in_pairs import ListNode


class Solution:
    def reverse_subgroup(self, group: ListNode):
        values = []

        while True:
            if not group or group.val is None:
                break

            values.append(group.val)
            group = group.next

        result = None

        for val in values:
            result = ListNode(val=val, next_=result)

        return result

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        result = ListNode()
        root = cur = ListNode()
        current = head
        done = False

        while True:
            for i in range(k):
                try:
                    cur.next = cur = ListNode(current.val)
                    current = current.next
                except AttributeError:
                    done = True
                    break

            if done:
                reversed_sub_group = root.next
            else:
                reversed_sub_group = self.reverse_subgroup(root.next)
            res_el = result

            while True:
                if not res_el.next:
                    res_el.next = reversed_sub_group
                    break
                res_el = res_el.next

            root = cur = ListNode()
            if done:
                break

        return result.next
