'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'ListNode: val={self.val}'


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return

        before = None
        node = head
        while node:
            tmp = node.next
            node.next = before
            before = node
            node = tmp
        return before

    def reverseList_recv(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = self.reverseList_recv(head.next)
        head.next.next = head
        head.next = None
        return node

    def reverseList_iter(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        current = head
        while current:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next

        return prev


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s = Solution()
    a = s.reverseList_iter(head)
    while a:
        print(a.val)
        a = a.next
