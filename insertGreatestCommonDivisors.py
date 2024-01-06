from typing import Optional

from pylist import ListNode


class Solution:
    def insertGreatestCommonDivisors(
            self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a % b)

        p = head

        while p is not None and p.next is not None:
            q = p.next
            p.next = ListNode(gcd(p.val, q.val))
            p.next.next = q
            p = q

        return head


head = [18, 6, 10, 3]
head = ListNode.fromList(head)
res = Solution().insertGreatestCommonDivisors(head)
ListNode.travel(res)
