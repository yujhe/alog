# Definition for a Node.
from typing import Deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        q = Deque()
        q.append(root)

        while q:
            n = len(q)

            next = None
            for _ in range(n):
                x = q.popleft()

                if not x:
                    continue

                x.next = next
                next = x

                q.append(x.right)
                q.append(x.left)

        return root

    def connectRecursive(self, root: Node) -> Node:
        if not root:
            return None

        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connectRecursive(root.left)
        self.connectRecursive(root.right)

        return root


if __name__ == '__main__':
    # given a perfect binary tree where all leaves on the same level,
    # connect the node.next to the right node in the same level
    #
    # Input: root = [1,2,3,4,5,6,7]
    # Output: [1,#,2,3,#,4,5,6,7,#]
    # Explanation: Given the above perfect binary tree,
    # your function should populate each next pointer to point to its next right node,
    # The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

    pass
