# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'Node:{self.val}'


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def _reverse(h: ListNode):
            first = ListNode(-1)
            while h:
                tmp = h.next
                h.next = first.next
                sec = ListNode(h.val)
                sec.next=h.next
                first.next = sec
                h = tmp
            return first.next

        r_head = _reverse(head)
        while head and r_head:
            if head.val != r_head.val:
                return False
            head = head.next
            r_head = r_head.next
        if head or r_head:
            return False
        return True


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    s = Solution()
    s.isPalindrome(head)
