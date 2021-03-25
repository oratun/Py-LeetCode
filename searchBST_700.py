"""
700. 二叉搜索树中的搜索
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
例如，
给定二叉搜索树:
        4
       / \
      2   7
     / \
    1   3
和值: 2
你应该返回如下子树:
      2
     / \
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from node import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """"""
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        elif val > root.val:
            return self.searchBST(root.right, val)

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """"""
        v_root = TreeNode(-1)
        v_root.right = root
        parent = v_root
        node = root
        while node:
            if node.val == key:
                break
            elif node.val > key:
                node = node.left
            else:
                node = node.right
            parent = node
        if not node:
            return root

        def find_max_from_left(node: TreeNode) -> TreeNode:
            """从BST树节点的左子树中找到值最大的节点"""
            if not node:
                return
            p = node
            node = node.left
            while node and node.right:
                p = node
                node = node.right
            p.right = None
            return node

        def find_min_from_right(node: TreeNode) -> TreeNode:
            """从BST树节点的右子树中找到值最小的节点"""
            if not node:
                return
            p = node
            node = node.right
            while node and node.left:
                p = node
                node = node.left
            p.left = None
            return node

        if node.left:
            max_sub_node = find_max_from_left(node)
            node.val = max_sub_node.val
        elif node.right:
            min_sub_node = find_min_from_right(node)
            node.val = min_sub_node.val
        else:
            if node.val < parent.val:
                parent.left =None
            else:
                parent.right = None
        return v_root.right
