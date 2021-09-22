# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        self._inorder(root, q, k)
        return q.pop()

    def _inorder(self, x: TreeNode, q: deque, k):
        if x == None:
            return

        self._inorder(x.left, q, k)
        if len(q) < k:
            q.append(x.val)
        else:
            return
        self._inorder(x.right, q, k)


if __name__ == '__main__':
    # given a binary serarch tree,
    # return the kth smallest element

    pass
