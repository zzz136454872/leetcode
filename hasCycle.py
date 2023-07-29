from typing import Optional

from pylist import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        p = head.next
        q = head

        while p != q and p is not None:
            p = p.next

            if p is None:
                return False

            if p == q:
                return True
            p = p.next
            q = q.next

        return p is not None and p == q


head = [3, 2, 0, -4]
pos = 1
head = ListNode.fromList(head)
head.next.next.next.next = head.next

head = [1, 2]
pos = 0
head = ListNode.fromList(head)
head.next.next = head

head = [1]
pos = -1
head = ListNode.fromList(head)

print(Solution().hasCycle(head))
