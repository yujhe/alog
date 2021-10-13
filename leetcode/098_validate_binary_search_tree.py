# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root, float('-inf'), float('inf'))

    def is_valid(self, node: TreeNode, lo: int, hi: int) -> bool:
        if not node:
            return True

        if node.val <= lo or node.val >= hi:
            return False

        return self.is_valid(node.left, lo, node.val) and self.is_valid(node.right, node.val, hi)


if __name__ == '__main__':
    # given a binary tree
    # return true if it is a binary search tree

    pass
