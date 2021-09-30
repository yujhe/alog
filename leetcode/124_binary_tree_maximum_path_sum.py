# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # the max path sum = root + max(0, left) + max(0, right)
        # track the max path sum so far and max sum to the node

        max_path_sum, _ = self.dfs(root)
        return max_path_sum

    def dfs(self, v) -> Tuple[int, int]:
        if not v:
            return float('-inf'), 0

        l_max_sum, max_sum_to_l = self.dfs(v.left)
        r_max_sum, max_sum_to_r = self.dfs(v.right)

        v_max_sum = max(l_max_sum, r_max_sum, v.val + max_sum_to_l + max_sum_to_r)
        max_sum_to_v = max(0, v.val + max(max_sum_to_l, max_sum_to_r))  # 0 means not take the node v to path

        return v_max_sum, max_sum_to_v


if __name__ == '__main__':
    # given a binary tree,
    # return the maximum path sum of a sequence of nodes
    # each node can only appear at most once

    pass
