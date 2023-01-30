from pylist import ListNode


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int,
                       list2: ListNode) -> ListNode:
        p = ListNode(-1)
        p.next = list1
        q = p

        for i in range(a):
            q = q.next
        r = q

        for i in range(b - a + 2):
            r = r.next
        q.next = list2

        while q.next != None:
            q = q.next
        q.next = r

        return p.next


list1 = [0, 1, 2, 3, 4, 5]
a = 3
b = 4
list2 = [1000000, 1000001, 1000002]
list1 = ListNode.fromList(list1)
list2 = ListNode.fromList(list2)
res = Solution().mergeInBetween(list1, a, b, list2)
ListNode.travel(res)
