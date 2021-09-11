from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return None

        # find the middle node
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # reverse the middle node
        prev = None
        cur = mid
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        reverse_head = prev

        # merge two list
        first = head
        second = reverse_head
        while second.next:
            next = first.next
            first.next = second
            first = next

            next = second.next
            second.next = first
            second = next

        return head
