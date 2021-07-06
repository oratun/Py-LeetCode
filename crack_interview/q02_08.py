# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return f'Node:{self.val}'


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        3,2,0,4,2,0,4,2,0,4
        3,0,2,4,0,2,4
        4, 8,3,6
        1,2,1,2,1,
        1,1,1,1,1
        t,n
        2x=x+t
        快慢指针相遇则有环,
        此时指针p从head出发，会与slow指针相遇在入环点
        '''
        if not head:
            return None
        if head.next == head:
            return head
        fast = slow = head
        first = second = 0
        while fast and fast.next:
            first += 1
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        p = head
        while p != slow:
            p = p.next
            slow = slow.next
        return p


if __name__ == '__main__':
    h = ListNode(3)
    h.next = ListNode(2)
    h.next.next = ListNode(0)
    h.next.next.next = ListNode(4)
    h.next.next.next.next = h.next

    s = Solution()
    print(s.detectCycle(h))
    # for k in range(8):
    #     l2 = list(range(1, 10))
    #     for i in range(len(l2)):
    #         l2[i] = ListNode(l2[i])
    #     for j in range(len(l2) - 1):
    #         l2[j].next = l2[j + 1]
    #     l2[-1].next = l2[k]
    #     print(s.detectCycle(l2[0]).val)
