from typing import Optional

from pylist import ListNode


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        tmp = []
        p = head

        while p != None:
            while len(tmp) > 0 and p.val > tmp[-1].val:
                tmp.pop()
            tmp.append(p)
            p = p.next

        for i in range(len(tmp) - 1):
            tmp[i].next = tmp[i + 1]
        tmp[-1].next = None

        return tmp[0]


head = [5, 2, 13, 3, 8]
head = [1, 1, 1, 1]
head = ListNode.fromList(head)
res = Solution().removeNodes(head)
ListNode.travel(res)
