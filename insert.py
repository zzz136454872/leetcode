from typing import List

from pylist import ListNode


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            head = ListNode(insertVal)
            head.next = head

            return head

        p = head.next
        q = head

        while p != head and p.val <= p.next.val:
            q = p
            p = p.next
        q = p
        p = p.next

        if p.val >= insertVal or q.val <= insertVal:
            q.next = ListNode(insertVal)
            q.next.next = p

            return head

        while p.val < insertVal:
            q = p
            p = p.next
        q.next = ListNode(insertVal)
        q.next.next = p

        return head


head = [3, 4, 1]
insertVal = 2
head = []
insertVal = 1
head = [1]
insertVal = 0
head = ListNode.fromList(head)

if head is not None:
    head.getTail().next = head
head = Solution().insert(head, insertVal)
ListNode.travel(head)
