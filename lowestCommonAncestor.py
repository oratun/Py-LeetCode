# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node:<{self.val}>'


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        node==p and (find(q, node.left) or find(q, node.right))
        node==q and (find(p, node.left) or find(p, node.right))
        find(p, node.left) and find(q, node.right)
        find(p, node.right) and find(q, node.left)
        """
        lca = None

        def find(root: TreeNode):
            nonlocal lca
            if not root:
                return False
            if root == p and (find(root.left) or find(root.right)):
                if lca is None:
                    lca = p
                return True
            if root == q and (find(root.left) or find(root.right)):
                if lca is None:
                    lca = q
                return True
            left_find = find(root.left)
            right_find = find(root.right)
            if left_find and right_find:
                if lca is None:
                    lca = root
                return True
            return root in [p, q] or left_find or right_find

        find(root)
        return lca


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    res = s.lowestCommonAncestor(root, root.left.left, root.left.right)
    print(res)
