# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.is_same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same(self, p, q):
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True

        return p.val == q.val and self.is_same(p.left, q.left) and self.is_same(p.right, q.right)


if __name__ == '__main__':
    # given two nodes
    # return true if node 2 is a sub tree of node 1

    t1 = TreeNode(3,  TreeNode(4),  TreeNode(5))
    t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(2, TreeNode(0))

    s = Solution().traverse_tree(t1)
    print(s)

    # pass
