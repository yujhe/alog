# Definition for a binary tree node.
from typing import Iterator


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # use preorder traversal: root -> left -> right
        path = []
        self.preorder_path(root, path)
        return ','.join(path)

    def preorder_path(self, x: TreeNode, path):
        if not x:
            path.append('#')  # use # to represent null node
            return

        path.append(str(x.val))
        self.preorder_path(x.left, path)
        self.preorder_path(x.right, path)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        return self.build(iter(data.split(',')))

    def build(self, node_vals: Iterator):
        # build tree in preorder
        n = next(node_vals)

        if n == '#':  # null node
            return None

        root = TreeNode(n)
        root.left = self.build(node_vals)
        root.right = self.build(node_vals)

        return root


if __name__ == '__main__':
    # the binary tree should be the same after serialize and deserialize
    # ser = Codec()
    # deser = Codec()
    # ans = deser.deserialize(ser.serialize(root))

    pass
