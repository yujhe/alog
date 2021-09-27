# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        i = 1
        while i < len(lists):
            for j in range(0, len(lists)-i, 2*i):
                lists[j] = self.merge(lists[j], lists[j+i])
            i *= 2

        return lists[0]

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.val < right.val:
            left.next = self.merge(left.next, right)
            return left
        else:
            right.next = self.merge(left, right.next)
            return right


if __name__ == '__main__':
    # given k linked list
    # return the merged linked list

    pass
