from heapq import heappop, heappush
from typing import List, Optional

from pylist import ListNode


def lt(self, other):
    return self.val < other.val


ListNode.__lt__ = lt


class Solution:
    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for lis in lists:
            if lis is not None:
                heappush(heap, lis)
        res = ListNode(-1)
        p = res

        while len(heap) > 0:
            now = heappop(heap)
            p.next = now
            p = p.next

            if p.next is not None:
                heappush(heap, p.next)
        p.next = None

        return res.next


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = []
lists = [[]]

for i in range(len(lists)):
    lists[i] = ListNode.fromList(lists[i])
ListNode.travel(Solution().mergeKLists(lists))
