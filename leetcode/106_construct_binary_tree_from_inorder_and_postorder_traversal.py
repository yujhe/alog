# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # postorder: left -> right -> root
        # inorder: left -> root -> right

        inorder_idx = {}
        for idx, v in enumerate(inorder):
            inorder_idx[v] = idx

        return self.build(postorder, len(postorder)-1, 0, len(inorder)-1, inorder_idx)

    def build(self, postorder, post_idx, in_left_idx, in_right_idx, in_idx):
        if post_idx < 0 or in_left_idx > in_right_idx:
            return None

        root = TreeNode(postorder[post_idx])
        right_nodes_num = in_right_idx - in_idx[root.val]

        # skip nodes in right sub-tree
        root.left = self.build(
            postorder, post_idx-right_nodes_num-1, in_left_idx, in_idx[root.val]-1, in_idx)

        root.right = self.build(postorder, post_idx-1,
                                in_idx[root.val]+1, in_right_idx, in_idx)

        return root


if __name__ == '__main__':
    # given two integer array,
    # one of the array is postorder traversal of the binary tree,
    # another one is inorder traversal of the binary tree
    # return the binary tree

    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    pass
