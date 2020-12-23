"""
107. 二叉树的层序遍历 II
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """"""
        if not root:
            return []
        return list(reversed(self.lob(root, [], 0)))

    def lob(self, root: TreeNode, res: List[List[int]], current_level: int):
        if len(res) <= current_level:
            res.append([])
        if root.left:
            self.lob(root.left, res, current_level + 1)
        if root.right:
            self.lob(root.right, res, current_level + 1)
        res[current_level].append(root.val)
        return res
