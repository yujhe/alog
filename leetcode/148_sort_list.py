# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sort(head)

    def sort(self, node: ListNode) -> ListNode:
        if not node or not node.next:
            return node

        # find mid node
        l, r = node, node.next
        while r and r.next:
            l = l.next
            r = r.next.next
        r = l.next
        l.next = None
        l = node

        sorted_l = self.sort(l)
        sorted_r = self.sort(r)

        return self.merge(sorted_l, sorted_r)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        head = dummy

        while left and right:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next

        head.next = left or right

        return dummy.next


if __name__ == '__main__':
    # given the head of a linked list,
    # return the list after sorting it in ascending order.

    pass
