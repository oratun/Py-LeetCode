"""
19. 删除链表的倒数第N个节点
难度 中等
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'Node({self.val})'


class Solution1:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = ListNode(0)
        first.next = head
        i = first
        j = first
        prev = first
        while n:
            j = j.next
            n -= 1
        while j:
            j = j.next
            prev = i
            i = i.next
        prev.next = i.next
        return first.next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = ListNode(0)
        first.next = head
        i = first
        j = first
        while n + 1:
            j = j.next
            n -= 1
        while j:
            j = j.next
            i = i.next
        i.next = i.next.next
        return first.next


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
n = 2
ret = s.removeNthFromEnd(head, n)
while ret:
    print(ret.val, end=',')
    ret = ret.next
