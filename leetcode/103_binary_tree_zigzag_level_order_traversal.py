# Definition for a binary tree node.
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        signal = 1  # 1: left to right, -1: right to left

        queue = Deque()
        queue.append(root)

        while queue:
            n = len(queue)
            level = []

            for _ in range(n):
                x = queue.pop()

                if not x:
                    continue

                level.append(x.val)

                queue.appendleft(x.left)
                queue.appendleft(x.right)

            if signal < 0:
                level.reverse()

            if level:
                order.append(level)

            signal *= -1

        return order


if __name__ == '__main__':
    # given a binary tree,
    # return the node values in zigzag level order traversal (from left to right, then right to left for the next level)

    pass
