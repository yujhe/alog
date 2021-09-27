# Definition for a binary tree node.
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # inorder: left -> root -> right
        # iterate root in preorder and find the left subtree, right subtree from inorder

        inorder_idx = {}
        for idx, v in enumerate(inorder):
            inorder_idx[v] = idx

        return self.build(preorder, 0, 0, len(inorder)-1, inorder_idx)

    # build tree from an array
    def build(self, preorder, pre_idx, in_left_idx, in_right_idx, in_idx):
        if pre_idx > len(preorder)-1 or in_left_idx > in_right_idx:
            return None

        root = TreeNode(preorder[pre_idx])
        left_nodes_num = in_idx[root.val] - in_left_idx

        root.left = self.build(
            preorder, pre_idx+1, in_left_idx, in_idx[root.val] - 1, in_idx)

        # skip left sub-tree nodes
        root.right = self.build(
            preorder, pre_idx+left_nodes_num+1, in_idx[root.val]+1, in_right_idx, in_idx)

        return root


def _inorder(x, q: Deque):
    if not x:
        return

    _inorder(x.left, q)
    q.append(x.val)
    _inorder(x.right, q)


def _preorder(x, q: Deque):
    if not x:
        return

    q.append(x.val)
    _preorder(x.left, q)
    _preorder(x.right, q)


if __name__ == '__main__':
    # given two integer array,
    # one of the arrays is preorder traversal of binary tree,
    # another one is inorder traversal of binary tree
    # return the binary tree

    preorder = [1, 2]
    inorder = [1, 2]

    solution = Solution()

    tree = solution.buildTree(preorder, inorder)
    q = Deque()
    _inorder(tree, q)

    assert inorder == list(q), f'inorder={list(q)} is not correct'

    q.clear()
    _preorder(tree, q)

    assert preorder == list(q), f'preorder={list(q)} is not correct'
