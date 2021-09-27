# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lo = min(p.val, q.val)
        hi = max(p.val, q.val)

        return self.dfs(root, lo, hi)

    def dfs(self, x, lo, hi):
        if x.val >= lo and x.val <= hi:
            return x

        if x.val < lo:
            return self.dfs(x.right, lo, hi)

        if x.val > hi:
            return self.dfs(x.left, lo, hi)


if __name__ == '__main__':
    # given a binary tree and two nodes
    # return the lowest common ancestor node

    pass
