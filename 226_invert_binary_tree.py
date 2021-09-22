# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs traverse nodes and reverse the child nodes
        q = deque()
        q.append(root)

        while q:
            x = q.popleft()

            if not x:
                continue

            t = x.left
            x.left = x.right
            x.right = t

            q.append(x.left)
            q.append(x.right)

        return root

    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)

    def dfs(self, x):
        if not x:
            return None

        t = x.left
        x.left = self.dfs(x.right)
        x.right = self.dfs(t)

        return x


if __name__ == '__main__':
    # given a binary tree,
    # return the root of reversed tree

    pass
