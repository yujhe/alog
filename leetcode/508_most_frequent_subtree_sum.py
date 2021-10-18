from typing import Counter, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()
        self.dfs(root, counter)

        max_count = max(counter.values)
        return [n for n in counter.keys() if counter[n] == max_count]

    def dfs(self, node: TreeNode, counter: Counter) -> int:
        if not node:
            return 0

        c = node.val + self.dfs(node.left, counter) + self.dfs(node.right, counter)
        counter[c] += 1
        return c


if __name__ == '__main__':
    # given a binary tree,
    # return the most frequent subtree sum (return all values if there is a tie)

    pass
