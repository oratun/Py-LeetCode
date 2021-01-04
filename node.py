# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'ListNode: val={self.val}'

    def mprint(self):
        node = self
        while node:
            print(node.val)
            node = node.next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'TreeNode: val={self.val}'
