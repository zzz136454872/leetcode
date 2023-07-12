from typing import Optional

from pylist import ListNode


class Solution:
    def removeZeroSumSublists(self,
                              head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(0)
        h.next = head
        mem = {}
        s = 0
        p = h

        while p != None:
            s += p.val
            mem[s] = p
            p = p.next
        p = h
        s = 0

        while p != None:
            s += p.val
            p.next = mem[s].next
            p = p.next

        return h.next


head = [1, 2, -3, 3, 1]
head = [1, 2, 3, -3, 4]
head = [1, 2, 3, -3, -2]
head = ListNode.fromList(head)
ListNode.travel(Solution().removeZeroSumSublists(head))
