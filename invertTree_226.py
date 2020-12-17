"""
226. 翻转二叉树
翻转一棵二叉树。
示例：
输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """recursive"""
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

    def invertTree_dfs(self, root: TreeNode) -> TreeNode:
        """non-recursive dfs stack"""
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

    def inverTree_brs(self, root: TreeNode) -> TreeNode:
        """bfs queue"""
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            node.left, node.right = node.right, node.left
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return root
