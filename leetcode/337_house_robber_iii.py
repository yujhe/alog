# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob, not_rob = self.dp(root)
        return max(rob, not_rob)

    def dp(self, node: TreeNode) -> tuple[int, int]:
        if not node:
            return (0, 0)

        rob_l, not_rob_l = self.dp(node.left)
        rob_r, not_rob_r = self.dp(node.right)

        rob = node.val + not_rob_l + not_rob_r
        not_rob = max(rob_l, not_rob_l) + max(rob_r, not_rob_r)

        return (rob, not_rob)


if __name__ == '__main__':
    # given a binary tree, you can not rob money from nodes in the same link
    # return the maximum amount of money you can rob

    pass
