from typing import Optional

from pylist import ListNode


def reverse(x):
    if x == None or x.next == None:
        return x
    p = x
    q = x.next
    p.next = None

    while q != None:
        r = q.next
        q.next = p
        p = q
        q = r

    return p


# addTwoNumbers
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = reverse(l1)
        l2 = reverse(l2)
        p = l1
        q = l2
        out = None
        start = None
        j = 0

        while p != None and q != None:
            now = p.val + q.val + j
            j = now // 10
            now = now % 10
            tmp = ListNode(now)

            if out != None:
                out.next = tmp

            if out == None:
                start = tmp
            out = tmp
            p = p.next
            q = q.next

        while p != None:
            now = p.val + j
            j = now // 10
            now = now % 10
            tmp = ListNode(now)

            if out != None:
                out.next = tmp

            if out == None:
                start = tmp
            out = tmp
            p = p.next

        while q != None:
            now = q.val + j
            j = now // 10
            now = now % 10
            tmp = ListNode(now)

            if out != None:
                out.next = tmp

            if out == None:
                start = tmp
            out = tmp
            q = q.next

        if j != 0:
            tmp = ListNode(j)
            out.next = tmp
            out = tmp

        return reverse(start)


l1 = [7, 2, 4, 3]
l2 = [5, 6, 4]
l1 = [0]
l2 = [0]
l1 = ListNode.fromList(l1)
l2 = ListNode.fromList(l2)
sl = Solution()
out = sl.addTwoNumbers(l1, l2)
ListNode.travel(out)


# 2. 两数相加
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        p = l1
        q = l2
        out = None
        start = None
        j = 0

        while p != None and q != None:
            now = p.val + q.val + j
            j = now // 10
            now = now % 10
            tmp = ListNode(now)

            if out != None:
                out.next = tmp

            if out == None:
                start = tmp
            out = tmp
            p = p.next
            q = q.next

        while p != None:
            now = p.val + j
            j = now // 10
            now = now % 10
            tmp = ListNode(now)

            if out != None:
                out.next = tmp

            if out == None:
                start = tmp
            out = tmp
            p = p.next

        while q != None:
            now = q.val + j
            j = now // 10
            now = now % 10
            tmp = ListNode(now)

            if out != None:
                out.next = tmp

            if out == None:
                start = tmp
            out = tmp
            q = q.next

        if j != 0:
            tmp = ListNode(j)
            out.next = tmp
            out = tmp

        return start


l1 = [2, 4, 3]
l2 = [5, 6, 4]
l1 = ListNode.fromList(l1)
l2 = ListNode.fromList(l2)
ListNode.travel(Solution().addTwoNumbers(l1, l2))
