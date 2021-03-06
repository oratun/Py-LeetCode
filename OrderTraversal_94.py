"""
二叉树前、中、后、层序遍历

这里使用的思想：已访问过的node，只将其val入栈
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node:{self.val}'


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, rst = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                rst.append(i)
        return rst

    def preOrderTraversal(self, root: TreeNode) -> List[int]:
        """前序遍历"""
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res

    def postOrderTraversal(self, root: TreeNode) -> List[int]:
        """后序遍历 经典法"""
        if not root:
            return []
        res, stack = [], []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == pre:
                res.append(root.val)
                pre = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res

    def postOrderTraversal2(self, root: TreeNode) -> List[int]:
        """后序遍历"""
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            if isinstance(root, int):
                res.append(root)
            else:
                stack.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """层序遍历 队列"""
        if not root:
            return []
        res = []
        dq = [root]
        while dq:
            root = dq.pop(0)
            res.append(root.val)
            if root.left:
                dq.append(root.left)
            if root.right:
                dq.append(root.right)
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """102.层序遍历 每层1个子列表 [[1],[2,3],]"""
        if not root:
            return []
        res = []
        self._levelOrder2(root, res)
        return res

    def _levelOrder2(self, root: TreeNode, res: List, level: int = 0):
        if not root:
            return []
        if len(res) <= level:
            res.insert(level, [])
        res[level].append(root.val)
        self._levelOrder2(root.left, res, level + 1)
        self._levelOrder2(root.right, res, level + 1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """107.层序遍历 自下往上 [[2,3], [1]]"""
        if not root:
            return []
        res = []
        self._levelOrderBottom(root, res, 0)
        return res

    def _levelOrderBottom(self, root: TreeNode, res: List, level: int) -> List[List[int]]:
        if not root:
            return []
        if len(res) <= level:
            res.insert(0, [])
        res[len(res) - level - 1].append(root.val)
        self._levelOrderBottom(root.left, res, level + 1)
        self._levelOrderBottom(root.right, res, level + 1)


if __name__ == '__main__':
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left.left = TreeNode(4)
    r.left.right = TreeNode(5)

    s = Solution()
    print(s.levelOrderBottom(r))
