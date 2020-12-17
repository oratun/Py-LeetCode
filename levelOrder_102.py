"""
102.二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
import queue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """bfs"""
        if not root:
            return []
        res = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            level = []
            for i in range(size):
                node = q.get()
                level.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            res.append(level)
        return res

    def levelOrder_recu(self, root: TreeNode) -> List[List[int]]:
        """递归 + dfs"""
        res = []
        return self.dfs(root, 0, res)

    def dfs(self, root: TreeNode, level: int, res: List[List[int]]) -> List[List[int]]:
        if not root:
            return
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level + 1, res)
        self.dfs(root.right, level + 1, res)
