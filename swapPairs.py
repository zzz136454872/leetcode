from typing import Optional

from pylist import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p = head
        head = head.next
        p.next = self.swapPairs(head.next)
        head.next = p

        return head


head = [1, 2, 3, 4]
head = []
head = [1]
head = ListNode.fromList(head)
ListNode.travel(Solution().swapPairs(head))
