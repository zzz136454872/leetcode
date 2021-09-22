from typing import List

from pylist import ListNode


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        l = 0
        p = head

        while p != None:
            p = p.next
            l += 1
        singleLen = l // k
        sub = l % k
        p = head
        out = []

        for i in range(k):
            out.append(p)
            t = p
            lenNow = singleLen

            if i < sub:
                lenNow += 1

            for j in range(lenNow):
                t = p
                p = p.next

            if lenNow != 0:
                t.next = None

        return out


head = [1, 2, 3]
k = 5
head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
out = Solution().splitListToParts(ListNode.fromList(head), k)

for i in range(k):
    ListNode.travel(out[i])
