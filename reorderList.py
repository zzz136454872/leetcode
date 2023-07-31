from typing import Optional

from pylist import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head == None:
            return
        p = head
        q = head

        while q != None:
            pre_p = p
            p = p.next
            q = q.next

            if q != None:
                q = q.next
        pre_p.next = None

        if p != None:
            q = p.next
            p.next = None

            if q != None:
                r = q.next

                while True:
                    q.next = p
                    p = q
                    q = r

                    if r != None:
                        r = r.next
                    else:
                        break
            q = p
            p = head

            while q != None:
                r = p.next
                p.next = q
                p = r
                r = q.next
                q.next = p
                q = r


head = [1, 2, 3, 4]
head = ListNode.fromList(head)
Solution().reorderList(head)
ListNode.travel(head)
