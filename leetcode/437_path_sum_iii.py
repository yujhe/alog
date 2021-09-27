# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # if we iterate nodes from 0 to n
        # we want to find a path that current prefix sum (from node 0 to node n) - x prefix sum (from node 0 to node x) = target
        # maintain a dictionary: prefix sum -> frequency
        # ex: nodes      1, 2, -1, -1, 2
        #     prefix sum 1, 3,  2,  1, 3
        #     target = 2
        # when we iterate to node 1 (val=2), we found that its prefix sum = 3, and the complement=3-2=1
        # so if we have prefix sum=1 in the dictionary, it means we can have a path after the node (prefix sum=1) to current node ({2})

        cur_sum = 0
        prefix_sum_paths = {0: 1}  # 0 means the root = the current node

        return self.dfs(root, cur_sum, prefix_sum_paths, targetSum)

    def dfs(self, x, prefix_sum, prefix_sum_paths, target):
        if not x:
            return 0

         # update the prefix sum from root to current node
        prefix_sum += x.val

        # get the # of paths that its prefix sum is the complement to target
        # ex: cur_prefix_sum = 2, target = 1, find the paths that its prefix sum = 2-1 = 1
        complement = prefix_sum - target
        paths = prefix_sum_paths.get(complement, 0)

        prefix_sum_paths[prefix_sum] = prefix_sum_paths.get(prefix_sum, 0) + 1

        paths += self.dfs(x.left, prefix_sum, prefix_sum_paths, target)
        paths += self.dfs(x.right, prefix_sum, prefix_sum_paths, target)

        prefix_sum_paths[prefix_sum] -= 1

        return paths


if __name__ == '__main__':
    # given a binary tree,
    # return all possible paths that sum up to target
    # the pathes sould go downward (from parent to child)

    pass
