"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth_recursive(self, root: TreeNode) -> int:
        """递归"""
        if not root:
            return 0
        return max(self.maxDepth_recursive(root.left), self.maxDepth_recursive(root.right)) + 1

    def maxDepth_dfs(self, root: TreeNode) -> int:
        """栈 深度优先"""
        if not root:
            return 0
        stack = [root]
        depth = 1
        depth_stack = [depth]
        while stack:
            node = stack.pop()
            tmp = depth_stack.pop()
            depth = max(depth, tmp)
            if node.right:
                stack.append(node.right)
                depth_stack.append(tmp + 1)
            if node.left:
                stack.append(node.left)
                depth_stack.append(tmp + 1)
        return depth

    def maxDepth_bfs(self, root: TreeNode) -> int:
        """队列广度优先"""
        if not root:
            return 0
        depth = 0
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                node = q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            depth += 1
        return depth


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.maxDepth_bfs(root))
