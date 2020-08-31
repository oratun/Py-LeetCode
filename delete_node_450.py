"""
450. 删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
示例:
root = [5,3,6,2,4,null,7]
key = 3
    5
   / \
  3   6
 / \   \
2   4   7
给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
    5
   / \
  4   6
 /     \
2       7
另一个正确答案是 [5,2,6,null,4,null,7]。
    5
   / \
  2   6
   \   \
    4   7
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f'node: val={self.val}'


class Solution:
    def predecessor(self, root: TreeNode) -> TreeNode:
        """
        返回左子节点中的最大节点(前驱节点）
        """
        node = root.left
        while node and node.right:
            node = node.right
        return node

    def successor(self, root: TreeNode) -> TreeNode:
        """
        返回右子节点中的最小节点(后驱节点)
        """
        node = root.right
        while node and node.left:
            node = node.left
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not (root.left or root.right):  # 没有子节点
                root = None
            elif root.right:  # 有右子节点
                root.val = self.successor(root).val
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root).val
                root.left = self.deleteNode(root.left, root.val)
        return root
    
    def inOrder(self, root: TreeNode) -> List:
        # 中序遍历
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right) if root else []


node5 = TreeNode(5)
node3 = TreeNode(3)
node6 = TreeNode(6)
node2 = TreeNode(2)
node4 = TreeNode(4)
node7 = TreeNode(7)

node5.left = node3
node5.right = node6
node3.left = node2
node3.right = node4
node6.right = node7

s = Solution()
n = s.deleteNode(node5, 3)
print(n)
