from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        q = deque()

        # bfs traverse nodes
        q.append((root, root.val))

        while q:
            x, max = q.popleft()

            if x == None:
                continue

            if x.val >= max:
                good += 1
                max = x.val

            q.append((x.left, max))
            q.append((x.right, max))

        return good


if __name__ == '__main__':
    # given a binary tree,
    # return the # of good nodes (good node: no nodes with a larger value from the root to the node)

    # Input: root = [3,1,4,3,null,1,5]
    # Output: 4
    # Explanation: Nodes in blue are good.
    # Root Node(3) is always a good node.
    # Node 4 -> (3, 4) is the maximum value in the path starting from the root.
    # Node 5 -> (3, 4, 5) is the maximum value in the path
    # Node 3 -> (3, 1, 3) is the maximum value in the path.

    pass
