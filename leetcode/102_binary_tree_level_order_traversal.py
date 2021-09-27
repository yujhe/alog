# Definition for a binary tree node.
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = Deque()

        q.append(root)

        while q:
            n = len(q)
            level = []
            for _ in range(n):
                x = q.popleft()

                if not x:
                    continue

                level.append(x.val)

                q.append(x.left)
                q.append(x.right)

            if level:
                ans.append(level)

        return ans


if __name__ == '__main__':
    # given a binary tree,
    # traverse the nodes in level order

    pass
