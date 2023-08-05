from typing import Optional

from pylist import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        p = res

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                p.next = list1
                p = list1
                list1 = list1.next
            else:
                p.next = list2
                p = list2
                list2 = list2.next

        p.next = list1

        while p.next is not None:
            p = p.next
        p.next = list2

        return res.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
l1 = []
l2 = []
l1 = []
l2 = [0]
l1 = ListNode.fromList(l1)
l2 = ListNode.fromList(l2)
ListNode.travel(Solution().mergeTwoLists(l1, l2))
